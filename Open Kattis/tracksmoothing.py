import sys
import math

def dist(p0, p1):
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N = inp[0][0]
    line = 1
    for i in range(N):
        R, V = inp[line]
        total_dist = 0
        x_0, y_0 = inp[line + 1]
        x0, y0, = x_0, y_0
        for i in range(line + 2,line + V + 1):
            x, y = inp[i]
            total_dist += dist((x0, y0), (x, y))
            x0, y0, = x, y

        total_dist += dist((x_0, y_0), (x, y))

        s = (total_dist - 2 * math.pi * R) / total_dist
        if s < 0:
            print("Not possible")
        else:
            print(s)

        line += V + 1

main()
        

    
