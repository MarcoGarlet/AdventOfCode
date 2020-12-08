fname='input.txt'
def read_file():
  global fname
  return [l.strip().split(':') for l in open(fname,'r').readlines()]

def count_valids(l):
  count=0
  for rule,passwd in l:
    yes,no = rule.split()[0].split('-')
    cons = rule.split()[1]
    yes,no=int(yes),int(no)
    if (passwd[yes]==cons and passwd[no]!=cons) or (passwd[yes]!=cons and passwd[no]==cons):
      count+=1
  return count

if __name__=='__main__':
  print(count_valids(read_file()))



