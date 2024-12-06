
import math
import random

from functools import reduce

def get_input(fname='input.txt'):
    with open(fname,'r') as f:
        content = f.readlines()
    rules = sorted([ [int(el) for el in l.strip().split('|')] for l in content if '|' in l])
    updates = [[int(el) for el in l.strip().split(',')] for l in content if ',' in l]
    return rules, updates


# TODO algoritmo di Kahn
def kahn_algo(rules, page_number):
    level_rules_edges = [rule for rule in rules if rule[0] in page_number and rule[1] in page_number]
    level_rules_nodes = list(set(reduce(lambda x,y: x+y, level_rules_edges)))

    level_rules_nodes_copy = level_rules_nodes.copy()
    grade_rules_nodes = {node: len([edge for edge in level_rules_edges if edge[1]==node]) for node in level_rules_nodes}
    
    solution = [el for el in page_number if el not in level_rules_nodes]
    #print(grade_rules_nodes)
    while (len(level_rules_nodes)>0):
        for node in level_rules_nodes_copy:
            if grade_rules_nodes[node] == 0 and node not in solution:
                solution.append(node)
                level_rules_nodes.remove(node)

                for edge in [e for e in level_rules_edges if e[0]==node]:
                    #print('update')
                    grade_rules_nodes[edge[1]]-=1
                #print(f"solution add {node}, grade {grade_rules_nodes}")
                #grade_rules_nodes = {node: len([edge for edge in level_rules_edges if edge[1]==node]) for node in level_rules_nodes}
            #print(solution)

    
    #print(f"level_rules_edges: {level_rules_edges} level_rules_nodes: {level_rules_nodes} page_number: {page_number}, solution = {solution}")

    return solution

    



def solve(rules, page_numbers):
    solutions = []
    for page_number in page_numbers:
        is_valid = False
        highlighted_rules = [r for r in rules if r[0] in page_number and r[1] in page_number]
        for rule in highlighted_rules:
            if page_number.index(rule[0])>page_number.index(rule[1]):
                #print(f"Non valido page_number: {page_number}, rule: {rule}, {page_number.index(rule[0])},{page_number.index(rule[1])}")        
                is_valid = True
                

        if is_valid:
            solutions.append(page_number)

    solutions = [kahn_algo(rules,solution) for solution in solutions]
    score = sum([solution[math.floor(len(solution)/2)] for solution in solutions])
    return score
        

if __name__ == '__main__':
    rules, page_numbers = get_input()#'example.txt')
    score = solve(rules, page_numbers)
    print(score)