from functools import reduce

fname = 'input.txt'


def readInput():
  line=[int(x) for x in open(fname,'r').readline().strip()]
  return [[line[25*i:25*i+25]for i in range(len(line)//25)][i1*6:i1*6+6] for i1 in range((len(line)//25)//6)]
    
def findMin(inp):
  mins,index_min = 25,0 # every line len  25
  for i in range(len(inp)):
    count0 = 0
    for l in inp[i]:
      count0+=l.count(0)
    if count0 < mins: 
      mins=count0
      index_min = i
  return index_min, mins
 
def layerNum12(layer):
  ones, twos = 0,0
  for l in layer:
    ones+=l.count(1)
    twos+=l.count(2)
  return ones*twos
   
  
       

if __name__=='__main__':
  inp = readInput()
  print(inp)
  index_min, mins = findMin(inp)
  print(inp[index_min])
  print(index_min)
  print(layerNum12(inp[index_min]))






