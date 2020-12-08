#fname = 'input.txt'
fname = 'test.txt'

def get_map():
  global fname
  return [l.strip() for l in open(fname, 'r').readlines()]

def sol(maps):
  i,c=0,0
  for l in maps[1:]:
    i+=3
    i%=len(l)
    if l[i]=='#': c+=1
  return c  

if __name__=='__main__':
  maps = get_map()
  print(sol(maps))
