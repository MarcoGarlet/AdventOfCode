from math import ceil

fname = 'input.txt'

def custom_unroll(forw):
  def row_unroll(c,l,r):
    if len(c)==1: return ceil((l+r)/2) if c[0]==forw else (l+r)//2
    else: return row_unroll(c[1:],ceil((l+r)/2),r) if c[0]==forw else row_unroll(c[1:],l,ceil((l+r)//2))
  return row_unroll

def get_id(r,c): return r*8+c

def sol():
  global fname
  c = []
  with open(fname,'r') as f:
    for l in f:
      l=l.strip()
      c+=[get_id(custom_unroll('B')(l[:-3],0,127),custom_unroll('R')(l[-3:],0,7))]
  return c
      

if __name__=='__main__':
  places = sol()
  full=[x for x in range(13,881)]
  print([c for c in full if c not in places][0])
  
