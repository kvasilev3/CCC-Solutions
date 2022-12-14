import sys

def j1():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print(0)
        return
    
    twenties_count = int(n / 20)
    remainder = n - (twenties_count * 20)
    if (remainder > 0 and remainder < 4) or remainder == 6 or remainder == 7 or remainder == 11:
        print(twenties_count)
        return
    
    print(twenties_count + 1)

if __name__ == '__main__':
    j1()
