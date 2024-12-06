guard_orientation = 'v<^>'
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
        new_guard_orientation = guard_orientation[(guard_orientation.index(matrix[guard_position[0]][guard_position[1]])+1)%len(guard_orientation)]
        matrix[guard_position[0]][guard_position[1]] = new_guard_orientation
        guard_move = guard_moves[new_guard_orientation]

    matrix[guard_position[0]][guard_position[1]] = '.'
    matrix[guard_position[0]+guard_move[0]][guard_position[1]+guard_move[1]] = new_guard_orientation

def get_guard_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] in guard_moves.keys():
                position = (i,j)
                break
    return position

def print_matrix(matrix):
    for l in matrix:
        for el in l:
            print(el, end = ' ')
        print()
    print('----------------------')

def is_position_in_matrix_boundaries(matrix,guard_position):
    return guard_position[0]!=0 and guard_position[0]!=len(matrix)-1 and guard_position[1]!=0 and guard_position[1]!=len(matrix[0])-1

def solve(matrix):
    guard_position = get_guard_position(matrix)
    path_guard = [str(guard_position)]

    while (is_position_in_matrix_boundaries(matrix, guard_position)):

        step(matrix, guard_position)
        guard_position = get_guard_position(matrix)
        path_guard.append(str(guard_position))

        #print_matrix(matrix)
    return len(set(path_guard))

if __name__ == '__main__':
    matrix = read_input()#'example.txt')
    score = solve(matrix)
    print(score)