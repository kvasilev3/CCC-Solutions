import sys
from typing import MutableMapping

violated_constraints = 0
must_be_together = dict()
must_be_separate = dict()


def add_to_must_be_together_dictionary(name1:str, name2:str):
    sorted_names = sorted([name1, name2])
    if sorted_names[0] not in must_be_together:
        must_be_together[sorted_names[0]] = []
    must_be_together[sorted_names[0]].append(sorted_names[1])


def add_to_must_be_separate_dictionary(name1:str, name2:str):
    sorted_names = sorted([name1, name2])
    if sorted_names[0] not in must_be_separate:
        must_be_separate[sorted_names[0]] = set()
    must_be_separate[sorted_names[0]].add(sorted_names[1])


def check_constraints(group_mate_1, group_mate_2, group_mate_3):
    global violated_constraints
    sorted_names = sorted([group_mate_1, group_mate_2, group_mate_3])
    for i in range(len(sorted_names)):
        if sorted_names[i] in must_be_together:
            matches = 0
            for mate_name in must_be_together[sorted_names[i]]:
                for j in range(i+1, len(sorted_names)):
                    if mate_name == sorted_names[j]:
                        matches += 1
            if matches < len(must_be_together[sorted_names[i]]):
                violated_constraints += (len(must_be_together[sorted_names[i]]) - matches)
        
        if sorted_names[i] in must_be_separate:
            for j in range(i+1, len(sorted_names)):
                if sorted_names[j] in must_be_separate[sorted_names[i]]:
                    violated_constraints += 1


def j4_alternative():
    # This method works, but the algorithm is cumbersome. It requires usage of multiple
    # structures and nested searches. I had to separate the logic in multiple fuctions
    # in order to make it cleaner. All functions above are used by this function.
    x = int(sys.stdin.readline().strip())
    for i in range(x):
        pair = sys.stdin.readline().strip().split(' ')
        add_to_must_be_together_dictionary(pair[0], pair[1])
    
    y = int(sys.stdin.readline().strip())
    for i in range(y):
        pair = sys.stdin.readline().strip().split(' ')
        add_to_must_be_separate_dictionary(pair[0], pair[1])
    
    g = int(sys.stdin.readline().strip())
    for i in range(g):
        group = sys.stdin.readline().strip().split(' ')
        check_constraints(group[0], group[1], group[2])

    print(violated_constraints)


def j4():
    # This the cleaner function. The whole logic is within this function. It converts
    # every pair of names into a tuple. It stores the rules into lists of tuples. Every 
    # student group is broken into 3 tuples of 2 names. All these tuples are stored
    # into the actual_pairs set. Then the function goes through the lists of rules and
    # checks if their tuples exist in the actual_pairs set.
    # Running time: O(x + y + g) - linear running time
    global violated_constraints

    must_be_together_list = []
    x = int(sys.stdin.readline().strip())
    for i in range(x):
        pair = sorted(sys.stdin.readline().strip().split(' '))
        must_be_together_list.append((pair[0], pair[1]))
    
    must_be_separate_list = []
    y = int(sys.stdin.readline().strip())
    for i in range(y):
        pair = sorted(sys.stdin.readline().strip().split(' '))
        must_be_separate_list.append((pair[0], pair[1]))
    
    g = int(sys.stdin.readline().strip())
    actual_pairs = set()
    for i in range(g):
        group = sorted(sys.stdin.readline().strip().split(' '))
        for i in range(len(group)-1):
            for j in range(i+1, len(group)):
                actual_pairs.add((group[i], group[j]))
    
    for together_rule in must_be_together_list:
        if together_rule not in actual_pairs:
            violated_constraints += 1
    for separate_rule in must_be_separate_list:
        if separate_rule in actual_pairs:
            violated_constraints += 1

    print(violated_constraints)


if __name__ == '__main__':
    #j4_alternative()
    j4()
