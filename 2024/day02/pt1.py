

def read_input(filename = 'input.txt'):
	with open(filename, 'r') as f:
		puzzle = [[int(el) for el in l.strip().split(' ')] for l in f.readlines()]
	return puzzle


def solve(puzzle):
	score = sum([1 for l in puzzle if (l == sorted(l) or l== sorted(l, reverse=True)) and len(set(l)) == len(l) and (len([abs(l[i]-l[i+1]) for i in range(len(l)-1) if abs(l[i]-l[i+1])>3 ])==0) ] )
	return score

if __name__ == '__main__':
	puzzle = read_input()
	score = solve(puzzle)
	print(score)
	
