import sys
from typing import MutableMapping

def j5_single_tree():
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


if __name__ == '__main__':
    #j5_single_tree()
    j5_small_area()
