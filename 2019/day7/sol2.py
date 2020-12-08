from pwn import *
from pc import *
from time import *
import threading
import queue
import itertools

q = queue.Queue()
r = queue.Queue()

def run(processes,ph):
  i2,i,e,r=0,0,0,0
  while True:
    log.info('i2={}'.format(i2))
    for p in processes:
      try:
        if r==0:
          p.sendline(str(ph[i]))
          i+=1
        p.sendline(str(i2)) 
        i2n=p.recvline().decode().strip()
        if i2n.isnumeric(): i2=i2n
      except EOFError:
        e=1 
        break
    if e==1: break
    r+=1
  for p in processes:
    try:
      p.close()
    except BrokenPipeError: continue
  log.info('CLEAN PROCS')
  return int(i2)
    


    


def runner():
  ph = q.get()
  log.info('Running {}'.format(ph))
  r.put(run([process('pc.py') for p in ph],ph))
  q.task_done()

 
 
if __name__=='__main__':
  phases = list(itertools.permutations(range(5,10),5))
  i,i1,lps,tr = 0,0,len(phases),5
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

