import sys

def main():
    inp = sys.stdin.read().splitlines()
    for instruction in inp[1:]:
        if instruction.startswith("Simon says"):
            print(instruction[10:])
        
main()
