
import math

def get_input(fname='input.txt'):
    with open(fname,'r') as f:
        content = f.readlines()
    rules = [ [int(el) for el in l.strip().split('|')] for l in content if '|' in l]
    updates = [[int(el) for el in l.strip().split(',')] for l in content if ',' in l]
    return rules, updates

def solve(rules, page_numbers):
    solutions = []
    for page_number in page_numbers:
        is_valid = True
        for rule in [r for r in rules if r[0] in page_number and r[1] in page_number]:
            if page_number.index(rule[0])>page_number.index(rule[1]):
                #print(f"Non valido page_number: {page_number}, rule: {rule}, {page_number.index(rule[0])},{page_number.index(rule[1])}")
                is_valid = False
                break
        if is_valid:
            solutions.append(page_number)
    score = sum([solution[math.floor(len(solution)/2)] for solution in solutions])
    return score
        

if __name__ == '__main__':
    rules, page_numbers = get_input()#'example.txt')
    score = solve(rules, page_numbers)
    print(score)