import sys

def main():

    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    ln = 0


    while True:
        N = inp[ln][0]
        if N == -1:
            break
        ln += 1
        hrs = 0
        dist = 0
        
        for i in range(N):
            [speed, time] = inp[ln + i]
            dist += speed * (time - hrs)
            hrs = time
        print(dist, "miles")

        ln += N

main()
