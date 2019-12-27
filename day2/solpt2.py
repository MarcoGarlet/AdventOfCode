from functools import reduce

'''
for 1 and 2: take two next integers apply the opcode 
and store at third next position

opcode:
  1  add
  2  mul
  99 halt


find noun and verb that produce 19690720
1 2 

'''


def computer(s,c):
  prog=[int(x) for x in s.split(',')]
  prog[1],prog[2] = c[0],c[1]
  i=0
  while i<len(prog):
    if prog[i] == 1:
      op1,op2=prog[prog[i+1]],prog[prog[i+2]]
      prog[prog[i+3]]=op1+op2
    elif prog[i] == 2:
      op1,op2=prog[prog[i+1]],prog[prog[i+2]]
      prog[prog[i+3]]=op1*op2
    else:
      break
    i+=4
  return prog
     


if __name__=='__main__':
  prog = open('input.txt','r').readlines()[0].strip()
  comb = reduce(lambda x,y: x+y, [[(x,y) for x in range(100)] for y in range(100)])
  for c in comb:
    if computer(prog,c)[0]==19690720:
      print('WIN = {}'.format(c))
      break
  exit()





