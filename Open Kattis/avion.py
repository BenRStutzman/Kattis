import sys

def main():
    inp = sys.stdin.read().splitlines()
    out = ""
    for i in range(len(inp)):
        if "FBI" in inp[i]:
            out += str(i + 1) + " "
    if out:
        print(out[:-1])
    else:
        print("HE GOT AWAY!")

main()
            
