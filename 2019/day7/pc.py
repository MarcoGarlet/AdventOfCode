#!/usr/bin/env python3
'''
for 1 and 2: take two next integers apply the opcode 
and store at third next position

opcode:
  1  add
  2  mul
  3  takes an integer and store at position of the only parameter
  4  output value at the address of the only parameter 
  5  jmp to op2 if op1 is != 0 
  6  jmp to op2 if op1 is == 0
  7  set op3 to 1 if op1<op2 else 0
  8  set op3 to 1 if op1==op2 else 0 
  99 halt
'''


expand_opcode = lambda x: ('0'*(5-len(x)))+x

def computer(s):
  prog=[int(x) for x in s.split(',')]
  i=0
  while i<len(prog):
    opcode = expand_opcode(str(prog[i]))
    if i+1 < len(prog):
      op1 = prog[i+1] if opcode[-3]=='1' else prog[prog[i+1]] if prog[i+1] < len(prog) else 0
    if i+2 < len(prog):
      op2 = prog[i+2] if opcode[-4]=='1' else prog[prog[i+2]] if prog[i+2] < len(prog) else 0
    if i+3 < len(prog):
      op3 = prog[i+3] if opcode[-5]=='1' else prog[prog[i+3]] if prog[i+3] < len(prog) else 0
     
    if int(opcode[-2:]) == 1:
      prog[prog[i+3]]=op1+op2
      i+=4
    elif int(opcode[-2:]) == 2:
      prog[prog[i+3]]=op1*op2
      i+=4
    elif int(opcode[-2:]) == 3:
      prog[prog[i+1]]=int(input())
      i+=2
    elif int(opcode[-2:]) == 4:
      print(op1)
      i+=2
    elif int(opcode[-2:]) == 5:
      if op1==0: i+=3
      else: i=op2
    elif int(opcode[-2:]) == 6:
      if op1!=0: i+=3
      else: i=op2
    elif int(opcode[-2:]) == 7:
      prog[prog[i+3]] = 1 if op1 < op2 else 0
      i+=4
    elif int(opcode[-2:]) == 8:
      prog[prog[i+3]] = 1 if op1==op2 else 0
      i+=4

    else:
      break
  return prog
     
if __name__=='__main__':
  prog = open('input.txt','r').readlines()[0].strip()
  computer(prog)






