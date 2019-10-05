import sys

def main():
    inp = sys.stdin.read().strip()
    total = 0
    for i in range(len(inp)):
        #print(inp[i])
        #print(inp[i + 1:] + inp[i])
        #print((inp[i + 1:] + inp[i]).index(inp[i]))
        next_same = (inp[i + 1:] + inp[i]).index(inp[i]) + i + 1
        #print(i, next_same)
        #print(len(set(inp[i + 1:next_same])))
        total += len(set(inp[i + 1:next_same]))
    print(total)
    

main()
