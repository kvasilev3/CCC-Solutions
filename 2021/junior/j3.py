import sys

def j3():
    previous_turn = 'N/A'
    for line in sys.stdin:
        line = line.strip()
        if line == '99999':
            return
        
        digit1 = int(line[0])
        digit2 = int(line[1])
        steps = int(line[2:])

        if (digit1 + digit2) % 2 > 0:
            turn = 'left'
        elif digit1 + digit2 > 0:
            turn = 'right'
        else:
            turn = previous_turn
        previous_turn = turn
        print('{0} {1}'.format(turn, steps))

if __name__ == '__main__':
    j3()
