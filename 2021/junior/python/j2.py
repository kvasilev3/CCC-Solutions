import sys

def j2():
    N = int(sys.stdin.readline().strip())
    max_bid_name = 'N/A'
    max_bid = 0
    for i in range(N):
        name = sys.stdin.readline().strip()
        bid = int(sys.stdin.readline().strip())
        if bid > max_bid:
            max_bid_name = name
            max_bid = bid
    print(max_bid_name)

if __name__ == '__main__':
    j2()
