
filename = 'input.txt'


orientation = {'R':lambda x,y: (x+1,y),\
               'U':lambda x,y: (x,y+1),\
               'D':lambda x,y: (x,y-1),\
               'L':lambda x,y: (x-1,y)}
              
modules = lambda x: -x if x<0 else x


def take_input():
  with open('input.txt','r') as f:
    for l in f:
      yield l.strip().split(',')  

def manhattan(p,q):
  s=0
  for o in zip(p,q):
    s+=modules(o[0]-o[1])
  return s

def get_points(path, path1):
  point_1 = [(0,0)]
  point_2 = [(0,0)]
  intersections=[]
  for directions in zip(path,path1):
    d1,d2 = directions[0], directions[1]
    for i in range(max([int(d1[1:]), int(d2[1:])])):
      point_1 += [orientation[d1[0]](point_1[-1][0],point_1[-1][1])] if i<int(d1[1:]) else []
      point_2 += [orientation[d2[0]](point_2[-1][0],point_2[-1][1])] if i<int(d2[1:]) else []
  point_1.remove((0,0))
  point_2.remove((0,0))
  return set(point_1).intersection(set(point_2)) 



if __name__=='__main__':
  paths = [x for x in take_input()]
  intersection = get_points(paths[0], paths[1])
  dst = []
  
  for p in intersection:
    dst+=[manhattan((0,0),p)]
  print(min(dst))   
  
  
   
  
  


