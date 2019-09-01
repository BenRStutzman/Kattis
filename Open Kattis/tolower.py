import sys

def main():
    inp = sys.stdin.read().splitlines()
    P, T = [int(num) for num in inp[0].split()]
    num_right = 0
    for problem in range(1, P * T + 1, T):
        #print('NEW PROBLEM')
        for case in range(problem, problem + T):
            string = inp[case]
            #print(string)
            if len(string) > 1 and not string[1:].islower():
                break
        else: num_right += 1

    print(num_right)
            
main()
