import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    cur_line = 1
    for i in range(N):
        n = int(inp[cur_line])
        #print(n)
        toys = {}
        for toy, m in [line.split() for line in inp[cur_line + 1: cur_line + 1 + n]]:
            toys[toy] = toys.get(toy, 0) + int(m)
        #print(toys)
        print(len(toys))
        output = sorted(toys.items(), key = lambda toy: toy[1], reverse = True)
        cur_num = output[0][1]
        group = set()
        for toy, num in output:
            if num == cur_num:
                group.add(toy)
            else:
                for other_toy in sorted(group):
                    print(other_toy, cur_num)
                group = {toy}
                cur_num = num
        for toy in sorted(group):
            print(toy, cur_num)
        cur_line += n + 1 

main()
