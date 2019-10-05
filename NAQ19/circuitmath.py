import sys

def main():
    inp = sys.stdin.read().splitlines()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    N = int(inp[0])
    vals = inp[1].split()
    stack = []
    for char in inp[2].split():
        if char in alpha:
            val = vals[alpha.index(char)]
            val = True if val == "T" else False
            stack.append(val)
        elif char in "*+-":
            if char == "*":
                A = stack.pop()
                B = stack.pop()
                stack.append(A and B)
                #print("test", stack)
            elif char == "+":
                A = stack.pop()
                B = stack.pop()
                stack.append(A or B)
            elif char == "-":
                stack.append(not stack.pop())
        #print(stack)
    output = "T" if stack[0] else "F"
    print(output)

main()
