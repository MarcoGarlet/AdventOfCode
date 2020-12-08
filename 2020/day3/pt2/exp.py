from functools import reduce

fname = 'input.txt'

def get_map():
  global fname
  return [l.strip() for l in open(fname, 'r').readlines()]

def sol(maps,right=3,down=1):
  r,c=0,0
  for i,l in enumerate(maps):
    if i%down!=0 or i==0: continue
    r+=right
    r%=len(l)
    if l[r]=='#': c+=1
  return c  

if __name__=='__main__':
  maps = get_map()
  moves = [(1,1),(3,1),(5,1),(7,1),(1,2)]
  sols = []
  for right,down in moves:
    sols+=[sol(maps,right,down)]
  print(sols)
  print(reduce(lambda x,y:x*y,sols))

