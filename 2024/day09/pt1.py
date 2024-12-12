from functools import reduce

def read_input(fname = 'input.txt'):
    with open(fname, 'r') as f:
        content = f.readline()
    return [int(c) for c in content]

def format(disk_map):
    return reduce(lambda x,y: x+y, [ ['.']*disk_map[i] if i%2!=0 else [f'{i//2}']*disk_map[i]  for i in range(len(disk_map))])

def sol(disk_map):
    str_map = ''.join(disk_map)
    free_spaces = str_map.count('.')
    i_free = 0
    i_last = len(disk_map)-1
    while len((''.join(disk_map)).split('.'*free_spaces))!=2:
        while disk_map[i_last]=='.':
            i_last-=1
        while disk_map[i_free]!='.':
            i_free+=1
        t = disk_map[i_last]
        disk_map[i_last] = disk_map[i_free]
        disk_map[i_free] = t
    
    return disk_map

def checksum(disk_map):
    return sum([int(disk_map[i])*i for i in range(len(disk_map)) if disk_map[i]!='.'])
    

if __name__ == '__main__':
    disk_map = read_input()#'example.txt')
    disk_map = format(disk_map)
    disk_map= sol(disk_map)
    print(checksum(disk_map))