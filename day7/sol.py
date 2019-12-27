from pwn import *
from pc import *

r = process('pc.py')



if __name__=='__main__':
  r.interactive()  

