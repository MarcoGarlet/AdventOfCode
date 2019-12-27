from functools import reduce

def checkpasswd(p):
  x=str(p)
  return reduce(lambda x,y:x and y,[int(x[i])<=int(x[i+1]) for i in range(len(x)-1)]) and  reduce(lambda x,y: x or y,[x.count(ch)==2 for ch in '0123456789'])


if __name__=='__main__':
  c=0
  for i in range(372037,905158):
    if checkpasswd(i): c+=1
  print(c)


