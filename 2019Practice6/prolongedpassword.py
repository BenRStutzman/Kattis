import sys

def main():
    inp = sys.stdin.read().splitlines()
    s = inp[0]
    strs = []
    for st in inp[1].split():
        strs.append(st)
    for st in inp[2].split():
        strs.append(st)
    #print(strs)
    k = int(inp[3])
    missing = []
    for num in inp[5].split():
        missing.append(int(num))
    #print(missing)
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in range(k):
        new = ""
        for ch in s:
            new += strs[alph.index(ch)]
        s = new
    #print(s)
    for m in missing:
        print(s[m-1])
    
main()
