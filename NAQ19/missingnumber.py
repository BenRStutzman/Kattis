import sys

def main():
    inp = sys.stdin.read().splitlines()
    numbers = int(inp[0])
    counted = inp[1:]
    end = int(counted[-1])
    if numbers == end:
        print("good job")
        return
    index = 0
    for i in range(1,end+1):
        if int(counted[index]) == i:
            index += 1
        else:
            print(i)

main()
