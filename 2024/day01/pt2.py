
def read_input(fname = 'input.txt'):
	with open(fname, 'r') as f:
		content = f.readlines()
	list1 = [int(line.split(' ')[0]) for line in content]
	list2 = [int(line.split(' ')[-1]) for line in content]
	
	score = sum([el*list2.count(el) for el in list1])

	return score
	


if __name__ == '__main__':
	score = read_input()
	print(score)
