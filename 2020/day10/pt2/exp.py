fname = 'data.txt'


def read():
  global fname
  l = [int(x) for x in open(fname, 'r').readlines()]
  s = [0]+sorted(l)+[max(l)+3]
  return s


sols = set()
res = {}
 
def sol(l):
  global sols,res
  if len(l)>2:
    for i in [i1 for i1 in range(len(l)-1) if abs(l[i1+1]-l[i1])<3]: 
      if abs(l[i]-l[i-1])+abs(l[i]-l[i+1])<=3 and l[:i]+l[i+1:] not in sols:
        sols.add(l[:i]+l[i+1:])
        sol(l[:i]+l[i+1:])
    sols.add(l)
         
    
    


if __name__=='__main__':
  l=tuple(read())
  sol(l)
  print(len(sols))
  #print(sols)
  
