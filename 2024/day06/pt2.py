from functools import reduce

guard_orientations = '^>v<'
guard_moves = {
    'v': (1,0),
    '<': (0,-1),
    '^': (-1,0),
    '>': (0,1),
}



def read_input(fname = 'input.txt'):
    with open(fname, 'r') as f:
        content = f.readlines()
    
    return [ list(l.strip()) for l in content]


def step(matrix, guard_position):
    guard_move = guard_moves[matrix[guard_position[0]][guard_position[1]]]
    new_guard_orientation = matrix[guard_position[0]][guard_position[1]]
    while matrix[guard_position[0]+guard_move[0]][guard_position[1]+guard_move[1]] == '#':
        new_guard_orientation = guard_orientations [(guard_orientations.index(new_guard_orientation)+1) %4]
        matrix[guard_position[0]][guard_position[1]] = new_guard_orientation
        guard_move = guard_moves[new_guard_orientation]

    matrix[guard_position[0]][guard_position[1]] = '.'
    matrix[guard_position[0]+guard_move[0]][guard_position[1]+guard_move[1]] = new_guard_orientation
    return new_guard_orientation

def get_guard_position(matrix, guard_orientation):
    position = [(matrix.index(l), l.index(guard_orientation)) for l in matrix if guard_orientation in l][0]
    return position

def print_matrix(matrix):
    for l in matrix:
        for el in l:
            print(el, end = ' ')
        print()
    print('----------------------')

def is_position_in_matrix_boundaries(matrix,guard_position):
    return guard_position[0]!=0 and guard_position[0]!=len(matrix)-1 and guard_position[1]!=0 and guard_position[1]!=len(matrix[0])-1




def simple_solve(matrix):
    guard_position = get_guard_position(matrix,'^')
    guard_orientation = matrix[guard_position[0]][guard_position[1]]

    path_guard = []

    while (is_position_in_matrix_boundaries(matrix, guard_position)):

        guard_orientation = step(matrix, guard_position)
        guard_position = get_guard_position(matrix, guard_orientation)
        
        path_guard.append(guard_position)

        #print_matrix(matrix)
    print(len(path_guard))
    #xit()
    return path_guard

def solve(matrix):
    guard_position = get_guard_position(matrix,'^')
    guard_orientation = matrix[guard_position[0]][guard_position[1]]

    path_guard = [str(guard_position)+"|"+str(guard_orientation)]
    is_in_loop = False
    steps = 0  
    while (is_position_in_matrix_boundaries(matrix, guard_position)):
        steps+=1
        #print(f"steps {steps}, max_steps {len(matrix) * len(matrix[0])}")
        guard_orientation = step(matrix, guard_position)
        guard_position = get_guard_position(matrix,guard_orientation)
        guard_orientation = matrix[guard_position[0]][guard_position[1]]
        if str(guard_position)+"|"+str(guard_orientation) in path_guard:
            is_in_loop = True
            break
        path_guard.append(str(guard_position)+"|"+str(guard_orientation))

        #print_matrix(matrix)
    return is_in_loop


def put_obstacles(matrix):
    solutions = []
    avanzamento = 0
    original_matrix = [l.copy() for l in matrix] # it's better to do a deep copy but this is enough

    interested_indexes = simple_solve([l.copy() for l in matrix])

    interested_indexes = set(interested_indexes)

    interested_indexes = [ el for el in interested_indexes if matrix[el[0]][el[1]] == '.' ]
    print(interested_indexes)


    for indexes in interested_indexes:
        i = indexes[0]
        j = indexes[1]
        avanzamento+=1
        print(f"avanzo {avanzamento}, totale {avanzamento}/{len(interested_indexes)}")
        matrix[i][j] = '#' # try to put obstacles
        
        if(solve(matrix)):
            solutions.append(str((i,j)))
        
        matrix = [l.copy() for l in original_matrix]

    return len(set(solutions))
    

if __name__ == '__main__':
    matrix = read_input()#'example.txt')
    score = put_obstacles(matrix)
    print(score)