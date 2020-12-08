fname='input.txt'
def read_file():
  global fname
  return [l.strip().split(':') for l in open(fname,'r').readlines()]

def count_valids(l):
  count=0
  for rule,passwd in l:
    mins,maxs = rule.split()[0].split('-')
    cons = rule.split()[1]
    mins,maxs=int(mins),int(maxs)
    if passwd.count(cons)>=mins and passwd.count(cons)<=maxs:
      count+=1
  return count

if __name__=='__main__':
  print(count_valids(read_file()))



