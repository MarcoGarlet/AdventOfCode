from functools import reduce

def read_input(fname = 'input.txt'):
    with open(fname, 'r') as f:
        content = f.readlines()
    return [list(l.strip()) for l in content]

def solve(content):
    possible_starts = [ [ (i,j) for j in range(len(content[0])) if content[i][j] == 'X' ] for i in range(len(content)) ]
    possible_starts = reduce(lambda x,y: x+y, possible_starts)
    solutions = []
    directions = [ (-1,-1),(0,-1),(1,-1),(1,0),(-1,0),(-1,1),(0,1),(1,1) ]
    for possible_start in possible_starts:
        for direction in directions:
            i = possible_start[0]
            j = possible_start[1]
            # for each direction start to build the possible strings, then we filter out xmas
            solution = 'X'
            for steps in range(1,4):            
                i+=direction[0]
                j+=direction[1]
                if(not (i in range(len(content)) and j in range(len(content[0])))):
                    break
                current_ch = content[i][j]
                solution+=current_ch
                steps+=1
            if solution == 'XMAS':
                solutions.append({'solution':solution,'coordinates':(possible_start[0],possible_start[1]), 'direction': direction})

    return solutions

if __name__ == '__main__':
    content = read_input()#'example.txt')
    solutions = solve(content)
    print(len(solutions))

    