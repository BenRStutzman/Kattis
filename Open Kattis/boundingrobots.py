import sys

def main():
    inp  = [line.split() for line in sys.stdin.read().splitlines()]
    ln = 0

    while True:
        if inp[ln] == ['0', '0']:
            break
        #print(inp[ln])
        width, length = [int(num) for num in inp[ln]]
        N = int(inp[ln + 1][0])
        x, y, think_x, think_y = 0, 0, 0, 0
        for ln in range(ln + 2, ln + N + 2):
            direc, dist = inp[ln]
            dist = int(dist)
            if direc == 'r':
                think_x += dist
                x = min(width - 1, x + dist)
            elif direc == 'l':
                think_x -= dist
                x = max(0, x - dist)
            elif direc == 'u':
                think_y += dist
                y = min(length - 1, y + dist)
            elif direc == 'd':
                think_y -= dist
                y =  max(0, y - dist)
        print("Robot thinks", think_x, think_y)
        print("Actually at", x, y)

        ln += 1
        
main()
