from functools import reduce

def read_input(fname = 'input.txt'):
    with open(fname, 'r') as f:
        content = f.readlines()
    return [list(l.strip()) for l in content]

def get_mas(content):
    possible_starts = [ [ (i,j) for j in range(len(content[0])) if content[i][j] == 'M' ] for i in range(len(content)) ]
    possible_starts = reduce(lambda x,y: x+y, possible_starts)
    all_mass = []
    directions = [ (-1,-1),(1,-1),(-1,1),(1,1) ]
    for possible_start in possible_starts:
        for direction in directions:
            i = possible_start[0]
            j = possible_start[1]
            # for each direction start to build the possible strings, then we filter out xmas
            solution = 'M'
            path = [(i,j)]
            for steps in range(1,3):            
                i+=direction[0]
                j+=direction[1]
                if(not (i in range(len(content)) and j in range(len(content[0])))):
                    break
                current_ch = content[i][j]
                solution+=current_ch
                steps+=1
                path.append((i,j))
            if solution == 'MAS':
                all_mass.append({'solution':solution,'path':sorted(path), 'processed': False})

    return all_mass


def is_cross(mass, other_mass):
    return mass[1]==other_mass[1] and mass[0][0] == other_mass[0][0] and mass[0][1] == other_mass[2][1] and mass[2][0]==other_mass[2][0] and mass[0][1] == other_mass[2][1]

def filter_diagonal(all_mass):
    solution=0
    for i_mass in range(len(all_mass)):
        mass = all_mass[i_mass]
        if not mass['processed']:
            diagonal = [other_mass for other_mass in all_mass if not other_mass['processed'] and is_cross(other_mass['path'],mass['path'])]
            if len(diagonal)>0:
                diagonal = diagonal[0]
                solution+=1
                diagonal['processed']=True
            mass['processed']=True

    return solution


if __name__ == '__main__':
    content = read_input()
    solution = filter_diagonal(get_mas(content))
    print(solution)

    