import sys

def j1():
    r = int(sys.stdin.readline().strip())
    s = int(sys.stdin.readline().strip())
    print((r*8) + (s*3) - 28)

if __name__ == '__main__':
    j1()
