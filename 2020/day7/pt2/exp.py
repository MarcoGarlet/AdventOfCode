import numpy as np

def read_file(fname):
  # read file and fill adj matrix
  # compute power of matrix to see how many nodes will bring you to G
  V,E = set(),{}
  with open(fname,'r') as f:
    for l in f:
      n,adj = [x.lstrip().rstrip() for x in l.split('contain')]
      V.add(n)
      for a in adj.split(','):
        if len(a.split())!=4: continue
        a=a.lstrip().rstrip().split()
        w=int(a[0])
        a=a[1]+' '+a[2]+' bags'
        V.add(a)
        E[(n,a)]=w
  return sorted(list(V)),E

def print_matrix(M):
  for l in M: print(l)

def to_matrix(V,E):
  return [[E[(u,v)] if (u,v) in E.keys() else 0 for v in V] for u in V]


zero = lambda x: all([all([l[i]==0 for i in range(len(x[0]))]) for l in x])
  
def sol(M,V):
  gold = 'shiny gold bags'
  golden_index = V.index(gold)
  answ = [[] for i in range(len(V))]
  M=np.array(M)
  MP=M.copy()
  while not all([x==0 for x in MP[golden_index]]):
    l_g=MP[golden_index]
    bags = [(i,l_g[i]) for i in range(len(MP[golden_index])) if l_g[i]>0]
    for i,w in bags:
      answ[i].append(w)
    MP=np.matmul(MP,M)
  return answ

if __name__=='__main__':
  fname = 'input.txt'
  V,E = read_file(fname)  
  M = to_matrix(V,E)
  answ=sol(M,V)
  print(sum([sum(x) for x in answ]))

