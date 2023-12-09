from functools import reduce



def read_file(fname):
	l = []
	with open(fname,'r') as f:
		l = f.readlines()

	races_time = l[0].strip().split(':')[1].strip().split()
	best_distances = l[1].strip().split(':')[1].strip().split()
	return [int(x) for x in races_time],[int(x) for x in best_distances]

def win_race(distance, time):
	win_possibilities = []
	for press_time in range(time-1,1,-1):
		if ((time-press_time)*press_time > distance):
			win_possibilities.append(press_time)

	return win_possibilities



if __name__=='__main__':
	races_time, best_distances = read_file('inp.txt')
	results = []	
	for race_time, best_distance in zip(races_time,best_distances):
		results.append(len(win_race(best_distance,race_time)))

	print(reduce(lambda x,y: x*y, results))
		


