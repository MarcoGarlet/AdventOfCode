import math

operators = ['+','*','']

def read_input(fname = 'input.txt'):
    with open(fname, 'r') as f:
        content = [ {'res': int(l.strip().split(':')[0]), 'numbers': [ int(n) for n in l.strip().split(':')[1].strip().split(' ')]}  for l in f.readlines()]
    return content

def to_tern(n):
    sol=''
    while n:
        sol+=str(n%3)
        n//=3
    return sol[::-1]
    
def solve(equations):
    solutions = []
    progress=0
    for equation in equations:
        print(f"{progress}/{len(equations)}")
        progress+=1
        res = equation['res']
        numbers = equation['numbers']
        assignment_length = math.ceil(math.log(3**(len(numbers)-1),3))
        possible_operations = [ '0'* (assignment_length-len(to_tern(i))) + to_tern(i) for i in range(3**(len(numbers)-1))]
        for possible_operation in possible_operations:
            eq = ''.join([str(numbers[i])+operators[int(possible_operation[i])] for i in range(len(numbers)-1)])
            eq_res = numbers[0]

            for i in range(1,len(numbers)-1):
                eq_res = eval(str(eq_res)+operators[int(possible_operation[i-1])]+str(numbers[i]))
                
            eq+=str(numbers[-1])
            eq_res = eval(str(eq_res)+operators[int(possible_operation[-1])]+str(numbers[-1]))
            
            if(res == eq_res):
                solutions.append(res)
                break
    
    return sum(solutions)

if __name__ == '__main__':
    equations = read_input()#'example.txt')
    solution = solve(equations)
    print(solution)