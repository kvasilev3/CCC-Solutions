import sys
from typing import MutableMapping

def j5_single_tree():
    # This solution earns 3 marks
    max_square_size = -1

    n = int(sys.stdin.readline().strip())
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        pair = sys.stdin.readline().strip().split(' ')
        r = int(pair[0])
        c = int(pair[1])

        possible_square_size = r-1
        if possible_square_size > max_square_size:
            max_square_size = possible_square_size
        possible_square_size = c-1
        if possible_square_size > max_square_size:
            max_square_size = possible_square_size
        possible_square_size = n-r
        if possible_square_size > max_square_size:
            max_square_size = possible_square_size
        possible_square_size = n-c
        if possible_square_size > max_square_size:
            max_square_size = possible_square_size

    print(max_square_size)

def j5_small_area():
    # This solution earns 5 marks
    max_square_size = -1

    n = int(sys.stdin.readline().strip())
    area = [[1 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        area[0][i] = 0
        area[i][0] = 0
    
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        pair = sys.stdin.readline().strip().split(' ')
        r = int(pair[0])
        c = int(pair[1])
        area[r][c] = 0

    for r in range(1, n+1):
        for c in range(1, n+1):
            if area[r][c] > 0:
                area[r][c] = min(area[r-1][c], area[r][c-1], area[r-1][c-1]) + 1
                if area[r][c] > max_square_size:
                    max_square_size = area[r][c]

    print(max_square_size)

class Tree:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Area:
    def __init__(self, row1, column1, row2, column2):
        self.row1 = min(row1, row2)
        self.column1 = min(column1, column2)
        self.row2 = max(row1, row2)
        self.column2 = max(column1, column2)
        self.sub_areas = []

    def contains(self, tree:Tree):
        return self.row1 <= tree.row and tree.row <= self.row2 and self.column1 <= tree.column and tree.column <= self.column2

    def generate_subareas(self, tree:Tree):
        new_areas = []
        if tree.row > self.row1:
            new_areas.append(Area(self.row1, self.column1, tree.row-1, self.column2))
        if tree.row < self.row2:
            new_areas.append(Area(tree.row+1, self.column1, self.row2, self.column2))
        if tree.column > self.column1:
            new_areas.append(Area(self.row1, self.column1, self.row2, tree.column-1))
        if tree.column < self.column2:
            new_areas.append(Area(self.row1, tree.column+1, self.row2, self.column2))
        self.sub_areas = new_areas

    def smaller_size(self):
        return min(self.row2 - self.row1 + 1, self.column2 - self.column1 + 1)

def process_area(area:Area, trees:list, tree_index:int):
    if area.contains(trees[tree_index]):
        area.generate_subareas(trees[tree_index])
        if tree_index+1 >= len(trees):
            # No more trees to process, just return the size of the largest possible square 
            # We calculate that by getting the smaller size of each rectangular area, and then 
            # taking the maximum of all
            return max([sa.smaller_size() for sa in area.sub_areas])
        
        max_possible_square_size = -1
        for sa in area.sub_areas:
            square_size = process_area(sa, trees, tree_index+1)
            if max_possible_square_size < square_size:
                max_possible_square_size = square_size
        return max_possible_square_size

    else:
        if tree_index+1 >= len(trees):
            # No more trees to process, just return the size of the largest possible square 
            # We calculate that by getting the smaller size of this rectangular area
            return area.smaller_size()
        
        return process_area(area, trees, tree_index+1)

def j5_recursive():
    # This solution earns 12 marks
    n = int(sys.stdin.readline().strip())
    
    t = int(sys.stdin.readline().strip())
    trees = list()
    for i in range(t):
        pair = sys.stdin.readline().strip().split(' ')
        r = int(pair[0])
        c = int(pair[1])
        trees.append(Tree(r, c))

    area = Area(1, 1, n, n)
    max_square_size = process_area(area, trees, 0)
    print(max_square_size)

if __name__ == '__main__':
    #j5_single_tree()
    #j5_small_area()
    j5_recursive()
