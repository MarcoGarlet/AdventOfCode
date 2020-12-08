from math import *
from functools import reduce
import operator

inp= '''
.#..#..#..#...#..#...###....##.#....\n
.#.........#.#....#...........####.#\n
#..##.##.#....#...#.#....#..........\n
......###..#.#...............#.....#\n
......#......#....#..##....##.......\n
....................#..............#\n
..#....##...#.....#..#..........#..#\n
..#.#.....#..#..#..#.#....#.###.##.#\n
.........##.#..#.......#.........#..\n
.##..#..##....#.#...#.#.####.....#..\n
.##....#.#....#.......#......##....#\n
..#...#.#...##......#####..#......#.\n
##..#...#.....#...###..#..........#.\n
......##..#.##..#.....#.......##..#.\n
#..##..#..#.....#.#.####........#.#.\n
#......#..........###...#..#....##..\n
.......#...#....#.##.#..##......#...\n
.............##.......#.#.#..#...##.\n
..#..##...#...............#..#......\n
##....#...#.#....#..#.....##..##....\n
.#...##...........#..#..............\n
.............#....###...#.##....#.#.\n
#..#.#..#...#....#.....#............\n
....#.###....##....##...............\n
....#..........#..#..#.......#.#....\n
#..#....##.....#............#..#....\n
...##.............#...#.....#..###..\n
...#.......#........###.##..#..##.##\n
.#.##.#...##..#.#........#.....#....\n
#......#....#......#....###.#.....#.\n
......#.##......#...#.#.##.##...#...\n
..#...#.#........#....#...........#.\n
......#.##..#..#.....#......##..#...\n
..##.........#......#..##.#.#.......\n
.#....#..#....###..#....##..........\n
..............#....##...#.####...##.\n
'''
BP = None
def str2array():
  array = []
  for l in inp.split():
    array+=[[x for x in l]]
  return array

def astPosition(array):
  ca=[] 
  for i in range(len(array)):
    for j in range(len(array[i])):
      if array[i][j]=='#': ca+=[(i,j)]
  return ca


def getBestPositions(asteroids):
  for asteroid in asteroids:
    atan2dict={}
    for ast in [x for x in asteroids if x!=asteroid]:
      k= atan2(asteroid[0]-ast[0], asteroid[1]-ast[1])
      if k not in atan2dict.keys():
        atan2dict[k]=[sqrt((asteroid[0]-ast[0])**2 + (asteroid[1]-ast[1])**2)]
      else: atan2dict[k]+=[sqrt((asteroid[0]-ast[0])**2 + (asteroid[1]-ast[1])**2)]
    if len(atan2dict.keys()) in atan2dict.keys(): counters[len(atan2dict.keys())]+=[asteroid]  
    else: counters[len(atan2dict.keys())]=[asteroid]
  return counters[max(counters.keys())]
  
def reachableFromPosition(asteroids, p):
  atan2dict={}
  for ast in [x for x in asteroids if x!=p]:
    k= atan2(p[0]-ast[0], p[1]-ast[1]) 
    if k not in atan2dict.keys():
      atan2dict[k]=[((ast[0]),(ast[1]))]
    else: atan2dict[k]+=[((ast[0]),(ast[1]))]
  return atan2dict
  

def vaporize(asteroids, bp):
  cv = 0
  deleted = []
  while cv < 200:
    
    asteroids = [x for x in asteroids if x not in deleted]
    de = reachableFromPosition(asteroids, bp)
    #deSortedK.sort()
    #deSortedK= deSortedK[::-1]
    point2delete = [de[k][0]  for k in de.keys()]
    
    center = BP
    print('center = {}'.format(center))
    zeroatan = None
    negativeatan ={} 
    positiveatan ={}
    for p in point2delete:
      if atan2(center[1]-p[1], center[0]-p[0])==0: zeroatan=p
      elif atan2(center[1]-p[1], center[0]-p[0])>0:
        k=atan2(center[1]-p[1], center[0]-p[0])
        positiveatan[k]=p  
      else:
        k=atan2(center[1]-p[1], center[0]-p[0])
        negativeatan[k]=p  
    # possible strategies: 1- delete all points in the same direction, then negative dec order, then positive inc order
    #det = (a.x - center.x) * (b.y - center.y) - (b.x - center.x) * (a.y - center.y)
    #center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), point2delete), [len(point2delete)] * 2))
    if zeroatan: 
      deleted.append(zeroatan)
      print('deleting {}'.format(zeroatan))
    cv+=1 
    if cv == 200:
      print(deleted[-1])
      break
    for k in sorted(negativeatan):
      deleted+=[negativeatan[k]]
      cv+=1
      print('deleting {}'.format(negativeatan[k]))
      if cv == 200:
        print(deleted[-1])
        break
    for k in sorted(positiveatan, reverse=True):
      deleted+=[positiveatan[k]]
      cv+=1
      print('deleting {}'.format(positiveatan[k]))
      if cv == 200:
        print(deleted[-1])
        break
      

 
if __name__=='__main__':
  array = str2array()
  asteroids = astPosition(array)
  counters = {}
  bestPosition= getBestPositions(asteroids)[0] 
  BP = bestPosition
  print('Best position to vaporize asteroids = {}'.format(bestPosition))  
  vaporize(asteroids, bestPosition)      
  print('COORDINATE IS Y X')
      
    
    
            
  
  
