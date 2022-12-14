import sys

def j1():
    for line in sys.stdin:
        b = int(line.strip())
        print(5 * b - 400)
        diff = b - 100
        if diff == 0:
            print('0')
        elif diff > 0:
            print('-1')
        else:
            print('1')

if __name__ == '__main__':
    j1()
