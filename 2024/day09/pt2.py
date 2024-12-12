from functools import reduce

def read_input(fname = 'input.txt'):
    with open(fname, 'r') as f:
        content = f.readline()
    return [int(c) for c in content]

def format(disk_map):
    return [ ['.']*disk_map[i] if i%2!=0 else [f'{i//2}']*disk_map[i]  for i in range(len(disk_map))]

def merge_space(disk_map):
    disk_map_copy = []
    free_blocks = [] 
    
    for i in range(len(disk_map)):
        if(disk_map[i][0]=='.'):
            free_blocks.append(disk_map[i])
        else:
            if(len(free_blocks)>0):
                free_blocks = list(reduce(lambda x,y:x+y, free_blocks))
                disk_map_copy.append(free_blocks)
                free_blocks = []
            disk_map_copy.append(disk_map[i])
    if len(free_blocks)>0:
        free_blocks = list(reduce(lambda x,y:x+y, free_blocks))
        disk_map_copy.append(free_blocks)

    return disk_map_copy


def sol(disk_map):
    i_last = len(disk_map)-1
    curr_block = str(max([int(disk_map[i][0]) for i in range(len(disk_map)) if disk_map[i][0]!='.']))

    while curr_block != disk_map[0][0]:
        free_blocks = [i for i in range(len(disk_map)) if disk_map[i][0]=='.' and len(disk_map[i])>=len(disk_map[i_last]) and i<i_last]
        if len(free_blocks)>0:
            free_block = free_blocks[0]
            remainder = ['.' for _ in range(len(disk_map[free_block])-len(disk_map[i_last]))]
            disk_map = disk_map[:free_block]+[disk_map[i_last]]+[remainder]+disk_map[free_block+1:i_last]+[['.' for i in range(len(disk_map[i_last]))]]+disk_map[i_last+1:]
        
            disk_map = [l for l in disk_map if len(l)>0]
            disk_map = [l for l in disk_map if len(l[0])>0]
            disk_map = merge_space(disk_map)

        curr_block = str(int(curr_block)-1)
        i_last = [i for i in range(len(disk_map)) if disk_map[i][0]==curr_block][0]

    
    return reduce(lambda x,y: x+y, disk_map)

def checksum(disk_map):
    return sum([int(disk_map[i])*i for i in range(len(disk_map)) if disk_map[i]!='.'])
    

if __name__ == '__main__':
    disk_map = read_input()#'example.txt')
    disk_map = format(disk_map)
    disk_map = [l for l in disk_map if len(l)>0]
    disk_map= sol(disk_map)


    print(checksum(disk_map))