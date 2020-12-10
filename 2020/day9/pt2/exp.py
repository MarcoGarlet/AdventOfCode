import itertools
from functools import reduce

fname = 'input.txt'

def read_file():
  global fname
  n = []
  with open(fname,'r') as f:
    for l in f:
      n+=[int(l)] 
  return n

def find_n(l):
  for i in range(25,len(l)):
    if not reduce(lambda x,y: x or y,(map(lambda x: (x[0]+x[1])==l[i],itertools.combinations(l[i-25:i],2)))): break
  return l[i]
    
def find_s(l,n):
  i,s,ss=0,0,[]
  while n>l[i]: i+=1
  i-=1
  while sum(ss)!=n:
    ss+=[l[i]]
    i-=1
    if sum(ss)>n:ss=ss[1:]
  return min(ss)+max(ss)

if __name__ == '__main__':
  l = read_file()
  n = find_n(l)
  print(find_s(l,n))

