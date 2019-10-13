import sys

def main():
    inp = sys.stdin.read().splitlines()
    prompt = inp[0]
    new,students,slots,capacity = (int(x) for x in inp[0].split())
    stored = [int(x) for x in inp[1].split()]
    toadd = [0 for i in range(slots)]
    for slot in sorted(range(slots), key = lambda x: stored[x]):
        add = min(new, capacity-stored[slot])
        new -= add
        toadd[slot] = add
    if sum([stored[s] for s in range(len(stored)) if toadd[s] == 0]) < students:
        print("impossible")
        return
    print(" ".join(str(x) for x in toadd))
        
main()
