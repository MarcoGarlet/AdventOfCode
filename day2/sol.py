'''
for 1 and 2: take two next integers apply the opcode 
and store at third next position

opcode:
  1  add
  2  mul
  99 halt
'''


def computer(s):
  prog=[int(x) for x in s.split(',')]
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
  print(computer(prog)) 





