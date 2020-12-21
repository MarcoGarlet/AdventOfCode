fname = 'data.txt'
gl = 0

def read():
  global fname,gl
  l = [int(x) for x in open(fname, 'r').readlines()]
  s = [0]+sorted(l)+[max(l)+3]
  gl = len(s)
  return s


sols = set()
res = {}

'''
recursive solution

def sol(l):
  global sols,res
  if len(l)>gl//3:
    for i in [i1 for i1 in range(len(l)-1) if abs(l[i1+1]-l[i1])<3]: 
      if abs(l[i]-l[i-1])+abs(l[i]-l[i+1])<=3 and l[:i]+l[i+1:] not in sols:
        sols.add(l[:i]+l[i+1:])
        sol(l[:i]+l[i+1:])
    sols.add(l)
'''      
def sol2(l):
  diff = [abs(l[i]-l[i+1]) for i in range(len(l)-1)]
  print(diff)  
  s = [[int(g) for g in x.strip().split(',') if len(g)>0] for x in str(diff)[1:-1].split('3') if len(x.split(','))>0]
  print(s)
  return 7**s.count([1,1,1,1])*4**s.count([1,1,1])*2**s.count([1,1])


if __name__=='__main__':
  l=tuple(read())
  print(sol2(l))
  
