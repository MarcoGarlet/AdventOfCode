
#fname='test.txt'
fname='input.txt'

def read_file():
  global fname
  g,buf=[],[]
  with open(fname,'r') as f:
    for l in f:
      if l=='\n':
        g+=[set(buf)]
        buf=[]
        continue
      buf+=[c for c in l.strip()]
  return g
        
def get_yes(g):
  s = 0
  for p in g:
    s+=len(p)
  return s
        



if __name__=='__main__':
  groups=read_file()
  print(get_yes(groups))
