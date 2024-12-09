import math
from functools import reduce

def read_input(fname='input.txt'):
    """
    Legge la mappa delle antenne da un file.
    """
    with open(fname, 'r') as f:
        content = f.readlines()
    return [list(l.strip()) for l in content]

def solve(matrix):
    """
    Calcola e proietta i punti antinodi per ogni coppia di antenne.
    """
    # Trova tutte le antenne nella matrice
    antennas = [[(i, j, matrix[i][j]) for j in range(len(matrix[0])) if matrix[i][j] != '.'] for i in range(len(matrix))]
    antennas = reduce(lambda x, y: x + y, antennas)

    print("Antenne trovate:", antennas)
    # Per ogni coppia di antenne, calcola le posizioni degli antinodi
    results = []
    for index_antenna1 in range(len(antennas)):
        for index_antenna2 in range(len(antennas)):
            p1 = antennas[index_antenna1]
            p2 = antennas[index_antenna2]
            if p1==p2 or p1[2]!=p2[2]:
                continue
            antinodes = antinodes_position(p1, p2, len(matrix[0]), len(matrix))  # Aggiungi limiti della matrice
            if len(antinodes)>0:
                results = [*results, *antinodes]
            #print(f"{p1}, {p2} => Antinodi: {antinodes}")
    print(results)
    return len(set(results))

def antinodes_position(p1, p2, width, height):

    x1, y1, s1 = p1
    x2, y2, s2 = p2
    
    vx, vy = x2 - x1, y2 - y1

    #print(f"vx= {vx}, vy= {vy}")

    antinode1 = (x1 - vx, y1 - vy)
    
    valid_antinodes = []
    ax, ay = antinode1
    while 0 <= ax < width and 0 <= ay < height:
        valid_antinodes.append((ax, ay))
        ax-=vx
        ay-=vy
    valid_antinodes.append((x1,y1))
    valid_antinodes.append((x2,y2))
    return valid_antinodes

def print_matrix(matrix):
    """
    Stampa la matrice in un formato leggibile.
    """
    for row in matrix:
        print(" ".join(row))
    print()

if __name__ == '__main__':
    # Lettura della matrice
    matrix = read_input()#'example.txt')
    print("Matrice originale:")
    print_matrix(matrix)
    
    # Risoluzione
    answer = solve(matrix)
    print("Risultato:", answer)
