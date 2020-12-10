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
       
def flush_reg():
  global regs
  for r in regs.keys(): regs[r]=0

def boot():
  global op,code_segment,regs,hist

  for sub in [(i,code_segment[i][0]) for i in range(len(code_segment)) if 'nop' in code_segment[i] or 'jmp' in code_segment[i]]: 
    ss = 'nop' if sub[1]=='jmp' else 'jmp'
    code_ss = code_segment.copy()
    code_ss[sub[0]]=[ss,code_ss[sub[0]][1]]
    flush_reg()
    hist=[]
    while regs['pc'] < len(code_ss):
      hist+=[regs['pc']]
      i,op1=code_ss[regs['pc']]
      op[i](int(op1))
      if regs['pc'] in hist: break
    if regs['pc'] == len(code_ss): break 
  return regs['acc']
  

if __name__ == '__main__':
  read_prog()
  print(boot())
