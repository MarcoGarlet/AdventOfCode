import string
#fname = 'test.txt'
fname = 'input.txt'

fields = {'ecl':lambda x: x in 'amb blu brn gry grn hzl oth'.split(),'pid':lambda x: len(x)==9 and all([c in string.digits for c in x]),'eyr':lambda x: len(x)==4 and x in [str(y) for y in range(2020,2031)],'hgt':lambda x: (x[-2:]=='cm' and x[:-2] in [str(c) for c in range(150,194)]) or (x[-2:]=='in' and x[:-2] in [str(c) for c in range(59,77)]) ,'byr':lambda x: len(x)==4 and x in [str(c) for c in range(1920,2003)],'iyr': lambda x:len(x)==4 and x in [str(c) for c in range(2010,2021)],'cid':lambda x:True,'hcl': lambda x:x[0]=='#' and all([c in [str(hex(d)).split('x')[1] for d in range(16)] for c in x[1:]]) and len(x[1:])==6}

def read_file():
  global fname
  i,c,s=0,[],''
  with open(fname,'r') as f:
    for l in f:
      if l=='\n':
        c+=[s]
        s=''
        continue
      s+=l
  return c

def sol(l):
  s=0
  for p in l:
    t = {}
    for f in p.split():
      k,v = f.split(':')
      t[k]=v
    if set(t.keys())==set(fields.keys()) or set(fields.keys()).difference(set(t.keys()))=={'cid'}:
      tab = []
      for k in t.keys():
        tab+=[fields[k](t[k])]
      if all(tab): s+=1
  return s
      


if __name__=='__main__':
  l = read_file()
  print(sol(l))
