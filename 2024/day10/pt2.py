from functools import reduce

def read_input(fname = 'input.txt'):
    with open(fname, 'r') as f:
        content = f.readlines()
    return [[int(n) for n in list(l.strip())] for l in content]

path_sol = {}
topology_map = read_input()#'example.txt')
directions = [(0,1),(0,-1),(1,0),(-1,0)]

def step(current,current_coordinate,current_start):
    if current==9:
        key = f"{current_start}-{current_coordinate}"
        if key not in path_sol.keys():
            path_sol[key]=1
        else:
            path_sol[key]+=1

    else:
        i = current_coordinate[0]
        j = current_coordinate[1]
        for direction in directions:
            i1 = i+direction[0]
            j1 = j+direction[1]
            if(i1 not in range(len(topology_map)) or j1 not in range(len(topology_map[0]))):
                continue
            if topology_map[i1][j1] == current+1:
                step(current+1,(i1,j1),current_start)

def sol():
    initial_steps = [[(i,j) for j in range(len(topology_map[0])) if topology_map[i][j] == 0] for i in range(len(topology_map))]
    initial_steps = reduce(lambda x,y: x+y, initial_steps)
    for initial_step in initial_steps:
        step(0,initial_step,initial_step)
    print(sum([path_sol[k] for k in path_sol.keys()]))
if __name__ == '__main__':
    sol()