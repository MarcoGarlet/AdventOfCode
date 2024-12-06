import re

def read_input(fname='input.txt'):
	with open(fname, 'r') as f:
		lines = f.readlines()
	return ''.join(lines)

def solve(line):
	pattern = r"mul\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"
	matches = [(int(el[0]),int(el[1]))for el in re.findall(pattern, line)]
	score = sum([ mul[0]*mul[1] for mul in matches])
	return score
if __name__ == '__main__':
	problem = read_input('example.txt')
	score = solve(problem)
	print(score)
