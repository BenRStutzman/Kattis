import sys

def main():
    inp = sys.stdin.read().splitlines()[1:]
    for line in inp:
        #print(line)
        total = sum([int(num) for num in line[::-2]])
        #print(total)
        for char in line[-2::-2]:
            num = int(char) * 2
            #print(num)
            if num < 10:
                total += num
            else:
                total += sum([int(dig) for dig in str(num)])
        if total % 10 == 0:
            print("PASS")
        else:
            print("FAIL")

main()
            
