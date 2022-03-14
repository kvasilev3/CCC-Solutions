import sys

def printCommand(line, commandStartIndex, signIndex, commandEndIndex):
    strings = line[commandStartIndex:signIndex]
    command = 'tighten' if line[signIndex] == '+' else 'loosen'
    turns = line[signIndex+1:commandEndIndex]
    print('{0} {1} {2}'.format(strings, command, turns))

def j3():
    line = sys.stdin.readline().strip()
    commandStartIndex = 0
    signIndex = -1
    for i in range(len(line)):
        if line[i] == '+' or line[i] == '-':
            signIndex = i
        elif signIndex >= 0:
            if (line[i] >= 'A' and line[i] <= 'Z'):
                printCommand(line, commandStartIndex, signIndex, i)
                commandStartIndex = i
                signIndex = -1
    printCommand(line, commandStartIndex, signIndex, i+1)

if __name__ == '__main__':
    j3()
