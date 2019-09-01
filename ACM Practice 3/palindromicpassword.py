import sys

def ispal(num):
    return str(num)[:3] == str(num)[5:2:-1]

def main():
    
    inp = [int(num) for num in sys.stdin.read().splitlines()]
    N = inp[0]
    for num in inp[1:]:
        diff = 0
        while True:
           if (num - diff) >= 100000 and ispal(num - diff):
               print(num - diff)
               break
           elif (num + diff) >= 100000 and ispal(num + diff):
               print(num + diff)
               break
           diff += 1
                
    
    
main()
