import sys

def main():
    inp = int(input())
    for i in range(inp, 1000000001):
        if not i % sum([int(num) for num in str(i)]):
            print(i)
            return
    
main()
