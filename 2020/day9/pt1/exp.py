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

def run(l):
  for i in range(25,len(l)):
    if not reduce(lambda x,y: x or y,(map(lambda x: (x[0]+x[1])==l[i],itertools.combinations(l[i-25:i],2)))): break
  return l[i]
    

if __name__ == '__main__':
  l = read_file()
  print(run(l))

