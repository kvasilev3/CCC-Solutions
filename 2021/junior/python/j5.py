from itertools import count
import sys

def j5_naive():
    M = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    canvas = [[False for i in range(N)] for j in range(M)]
    K = int(sys.stdin.readline().strip())
    for i in range(K):
        command = sys.stdin.readline().strip().split(' ')
        commandArgument = int(command[1]) - 1
        if command[0] == 'R':
            row = commandArgument
            for col in range(N):
                canvas[row][col] = not canvas[row][col]
        elif command[0] == 'C':
            col = commandArgument
            for row in range(M):
                canvas[row][col] = not canvas[row][col]
    
    goldenTilesCount = 0
    for row in range(M):
        for col in range(N):
            if canvas[row][col]:
                goldenTilesCount += 1
    print(goldenTilesCount)

def j5():
    M = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())
    rowCommands = dict()
    colCommands = dict()
    for i in range(K):
        command = sys.stdin.readline().strip().split(' ')
        commandArgument = int(command[1]) - 1
        if command[0] == 'R':
            row = commandArgument
            if row not in rowCommands:
                rowCommands[row] = 0
            rowCommands[row] += 1
        elif command[0] == 'C':
            col = commandArgument
            if col not in colCommands:
                colCommands[col] = 0
            colCommands[col] += 1
    
    goldenTilesCount = 0
    for row in range(M):
        for col in range(N):
            if row in rowCommands:
                rowCount = rowCommands[row]
            else:
                rowCount = 0
            if col in colCommands:
                colCount = colCommands[col]
            else:
                colCount = 0
            if (rowCount + colCount) % 2 != 0:
                goldenTilesCount += 1
    print(goldenTilesCount)

if __name__ == '__main__':
    j5()
