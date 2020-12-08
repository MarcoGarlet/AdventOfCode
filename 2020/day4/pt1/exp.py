
#fname = 'test.txt'
fname = 'input.txt'

fields = {'ecl','pid','eyr','hcl','byr','iyr','cid','hgt'}

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
  print(l)
  for p in l:
    t = set()
    for f in p.split():
      print(f)
      k,v = f.split(':')
      t.add(k)
    if t==fields or fields.difference(t)=={'cid'}:
      s+=1
  return s
      


if __name__=='__main__':
  l = read_file()
  print(sol(l))
