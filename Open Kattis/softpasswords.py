import sys

def reverse_case(S):
    P = ""
    for char in S:
        if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if char.islower():
                P += char.upper()
            elif char.isupper():
                P += char.lower()
        else:
            P += char
    return P
        

def main():
    S, P = sys.stdin.read().splitlines()
    if P == S:
        print("Yes")
        return
    for i in range(10):
        if P + str(i) == S or str(i) + P == S:
            print("Yes")
            return
    if P == reverse_case(S):
        print("Yes")
        return
    print("No")

main()
    
