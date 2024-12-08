import math
operators = ['+','*']

def read_input(fname = 'input.txt'):
    with open(fname, 'r') as f:
        content = [ {'res': int(l.strip().split(':')[0]), 'numbers': [ int(n) for n in l.strip().split(':')[1].strip().split(' ')]}  for l in f.readlines()]
    return content

def solve(equations):
    solutions = []

    for equation in equations:
        res = equation['res']
        numbers = equation['numbers']
        assignment_length = int(math.log(2**(len(numbers)-1),2))
        possible_operations = [ '0'* (assignment_length-len(bin(i).split('b')[1])) + bin(i).split('b')[1] for i in range(2**(len(numbers)-1))]
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