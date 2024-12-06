
def read_input(fname = 'input.txt'):
	with open(fname, 'r') as f:
		content = f.readlines()
	
	return sorted([int(line.split(' ')[0]) for line in content]), sorted([int(line.split(' ')[-1]) for line in content])
	


if __name__ == '__main__':
	list1, list2 = read_input()
	print(sum([abs(list1[i]-list2[i]) for i in range(len(list1))]))
