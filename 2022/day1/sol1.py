
fname = './inp.txt'

def read_calories():
	l = None
	with open(fname,'r') as f:
		l = [sum([int(x) for x in x.split()]) for x in f.read().split('\n\n')]

	return l




if __name__ == '__main__':
	l = read_calories()
	print(max(l))
