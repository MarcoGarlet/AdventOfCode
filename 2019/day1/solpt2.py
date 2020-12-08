



def getfuel4module(module):
  if module//3-2>0:
    return (module//3-2)+getfuel4module(module//3-2)
  else: return 0  





if __name__=='__main__':
  tot=0
  with open('input.txt', 'r') as f:
    for l in f:
      el=getfuel4module(int(l.strip()))
      print('module = {}, fuel={}'.format(l.strip(),el))
      tot+=el
  print('Tot= {}'.format(tot))
      





