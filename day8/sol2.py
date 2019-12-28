from functools import reduce
import numpy as np
from PIL import Image


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
   
  
def extractImage(inp):
  print('len of inp = {}, len of line of inp = {}'.format(len(inp),len(inp[0])))
  indexes = reduce(lambda x,y: x+y, [[(i1,i) for i in range(25)] for i1 in range(6)])
  matrix = [[0 for i in range(25)] for i1 in range(6)]
  i = 0
  for ind in indexes:
    for layer in inp:
      if layer[ind[0]][ind[1]] in [0,1]:
        matrix[ind[0]][ind[1]]= (0,0,0) if layer[ind[0]][ind[1]]==1 else (255,255,255)
        break
  return matrix
    
  



if __name__=='__main__':
  inp = readInput()
  print('len(inp)={}, len(inp[0]) = {}, len(inp[0][0]) = {}'.format(len(inp),len(inp[0]), len(inp[0][0])))
  m=extractImage(inp)
  print(m)
  array = np.array(m, dtype=np.uint8)
  new_image = Image.fromarray(array)
  new_image.save('message.png')  
  



