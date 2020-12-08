from pwn import *
from pc import *
from time import *
import threading
import queue
import itertools

q = queue.Queue()
r = queue.Queue()

def run(ph):
  outs = []
  in2 = '0'
  
  for p in ph:
    r = process('./pc.py')
    r.sendline(str(p))
    r.sendline(in2) 
    in2=r.recvline()
    in2=in2.decode()
    r.close()
  return int(in2) 

def runner():
  ph = q.get()
  log.info('Running {}'.format(ph))
  r.put(run(ph))
  q.task_done()

 
 
if __name__=='__main__':
  phases = list(itertools.permutations(range(5),5))
  i,i1,lps,tr = 0,0,len(phases),200
  poll  = []
  for ph in phases:
    q.put(ph)
    t = threading.Thread(target=runner)
    poll+=[t]
    t.start()
    log.info('COMPLETE {}'.format(i1))
    if i==tr:
      for t1 in poll:
        t.join()
        i=0
        tr-=1 if tr>1 else 1
        
    i+=1
    i1+=1

  q.join()
  signals = [r.get() for i in range(len(phases))] 
  print('MAX = {}'.format(max(signals))) 

