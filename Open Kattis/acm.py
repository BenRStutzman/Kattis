import sys

def main():
    inp = [line.split() for line in sys.stdin.read().splitlines()]
    answered = {}
    for line in inp[:-1]:
        T, Q, R = int(line[0]), line[1], line[2]
        if Q in answered:
            answered[Q][0] = R
            answered[Q][1] += T if R == "right" else 20
        else:
            answered[Q] = [R, T] if R == "right" else [R, 20]
    correct = 0
    total_time = 0
    for question in answered.values():
        if question[0] == "right":
            correct += 1
            total_time += question[1]
    print(correct, total_time)
        
    

    
main()
