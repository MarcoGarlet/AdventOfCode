
  




if __name__=='__main__':
  tot=0
  with open('input.txt','r') as f:
    for l in f:
      tot+=(int(l.strip())//3)-2
  print('Tot= {}'.format(tot))     

