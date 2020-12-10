#fname = 'test.txt'
fname = 'input.txt'

regs = {'acc':0,'pc':0}

def nop(x): regs['pc']+=1
def jmp(x): regs['pc']+=x
def acc(x): 
  regs['acc']+=x 
  nop(x)

op = {'nop':nop,'jmp':jmp,'acc':acc}
hist = []
code_segment = []


def read_prog():
  global fname,code_segment
  with open(fname,'r') as f:
    for i,l in enumerate(f):
      code_segment+=[l.strip().split()]
       

def run():
  global op,code_segment,regs,hist
  while regs['pc'] not in hist:
    hist+=[regs['pc']]
    i,op1=code_segment[regs['pc']]
    #print(i,op1)
    op[i](int(op1))
  return regs['acc']
  

if __name__ == '__main__':
  read_prog()
  print(run())
