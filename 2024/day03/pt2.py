import re

def read_input(fname='input.txt'):
	with open(fname, 'r') as f:
		lines = f.readlines()
	return ''.join(lines)

def solve(line):
	pattern = r"mul\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)|(do|don't)\s*\(\s*\)"
	matches = [(int(el[0]),int(el[1])) if el[2] == '' else True if el[2] == 'do' else False for el in re.findall(pattern, line)]
	score = 0
	enabled = True
	for match in matches:
		if(type(match) == type(False)):
			enabled = match
			continue
		if enabled:
			score+=(match[0]*match[1])
	return score
	
if __name__ == '__main__':
	problem = read_input()
	score = solve(problem)
	print(score)
