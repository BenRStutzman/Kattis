import sys

def main():
    inp  = [line.split() for line in sys.stdin.read().splitlines()]
    circles = []
    rects = []
    for ln in range(1, int(inp[0][0]) + 1):
        if inp[ln][0] == "circle":
            circles.append([int(num) for num in inp[ln][1:]])
        else:
            rects.append([int(num) for num in inp[ln][1:]])

    #print(circles)
    #print(rects)

    for x, y in [[int(num) for num in line] for line in inp[ln + 2:]]:
        #print("NEW SHOT:", x, y)
        num_hit = 0
        for x1, y1, r in circles:
            if (x - x1) ** 2 + (y - y1) ** 2 <= r ** 2:
                #print("hit circle:", x1, y1, r)
                num_hit += 1
        for x1, y1, x2, y2 in rects:
            if x1 <= x <= x2 and y1 <= y <= y2:
                #print("hit rect:", x1, y1, x2, y2)
                num_hit += 1

        print(num_hit)   
    
main()
