import itertools
fname='./input.txt'

def read_file():
  global fname
  numbers = open(fname,'r').readlines()
  return [int(x.strip()) for x in numbers]

def get_2020(numbers):
  for el0,el1,el2 in itertools.combinations(numbers,3):
    if el0+el1+el2==2020:
      return el0*el1*el2

if __name__=='__main__':
  print(get_2020(read_file()))
  

