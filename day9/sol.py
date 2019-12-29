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
pc=0
rbase = 0


prog = open('input.txt','r').readlines()[0].strip()
prog=[int(x) for x in prog.split(',')]
memory={i:prog[i] for i in range(len(prog))} # tutti i parametri ora passano dalla memoria 
print(len(prog))
'''
1,2,7,8 = 3 parametri
5,6 = 2 parametri
3,4,9 = 1 parametro
'''




'''
Se un parametro caricato in memoria è presente nel programma, devi aggiornare quello in memoria

'''

def computer(s):
  global pc,rbase
  #print(prog)  
  while pc<len(prog):
    #input('Continue? ')
    #print('-----------MEMDUMP-----------')
    #print(memory)
    #print('PC = {}'.format(pc))
    #print('-----------------------------')
    opcode = expand_opcode(str(prog[pc]))
    instruction = int(opcode[-2:])
    # 1 op is mandatory
    mode1 = opcode[-3]
    base = 0 if mode1 == '0' else rbase
    if pc+1 not in memory.keys(): memory[pc+1]=0
    if mode1 in '02':
      position = memory[pc+1] + base
      if position not in memory.keys(): memory[position]=0
      op1,add1 = memory[position],position
    if mode1 == '1':
      op1,add1 = memory[pc+1],pc+1
       
    
    if instruction in [1,2,7,8]+[5,6]:
      mode2 = opcode[-4]
      base = 0 if mode2 == '0' else rbase
      if pc+2 not in memory.keys(): memory[pc+2]=0
      if mode2 in '02':
        position = memory[pc+2] + base
        op2 = memory[position] 
      if mode2 == '1':
        op2 = memory[pc+2]
 
      if instruction in [1,2,7,8]:
        mode3 = opcode[-5]
        base3 = 0 if mode3 == '0' else rbase
        if pc+3 not in memory.keys(): 
          memory[pc+3]=0  
        op3 = memory[pc+3]+base3
        
 
    if instruction == 1:
      memory[op3]=op1+op2
      pc+=4
    elif instruction == 2:
      memory[op3]=op1*op2
      pc+=4
    elif instruction == 3:
      memory[add1]=int(input())
      pc+=2
    elif instruction == 4:
      print(op1)
      pc+=2
    elif instruction == 5:
      if op1==0: pc+=3
      else: pc=op2
    elif instruction == 6:
      if op1!=0: pc+=3
      else: pc=op2
    elif instruction == 7:
      memory[op3] = 1 if op1 < op2 else 0
      pc+=4
    elif instruction == 8:
      memory[op3] = 1 if op1==op2 else 0
      pc+=4
    elif instruction == 9:
      rbase += op1
      pc+=2  

    else:
      break
  return prog
     


if __name__=='__main__':
  computer(prog)





