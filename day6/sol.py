
filename = 'input.txt'

V = set()
E = {}
root = None

def printGraph():
  for v in E.keys():
    print('{} -> {}'.format(v,E[v]))

def readGraph():
  with open(filename, 'r') as f:
    for l in f:
      node,edge = l.split(')')[0], l.split(')')[1].strip()
      V.add(node)
      V.add(edge)
      if node not in E.keys():
        E[node]=[]
      E[node]+=[edge]

def pathLen(node,k=0):
  for n in E.keys():
    if node in E[n]:
      k=pathLen(n,k+1)
  return k
  
if __name__=='__main__':
  readGraph()
  printGraph()
  pl = 0   
  root = list(E.keys())[0]
  for k in V:
    sk=pathLen(k) 
    print('k={}, step = {}'.format(k,sk))
    pl+=sk
  print(pl)
  


