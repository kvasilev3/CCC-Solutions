import sys

def j2():
    n = int(sys.stdin.readline().strip())
    starPlayersCount = 0
    for i in range(n):
        pointsScored = int(sys.stdin.readline().strip())
        foulsCommitted = int(sys.stdin.readline().strip())
        stars = (pointsScored * 5) - (foulsCommitted * 3)
        if stars > 40:
            starPlayersCount += 1
    print(str(starPlayersCount) + ('+' if starPlayersCount == n else ''))

if __name__ == '__main__':
    j2()
