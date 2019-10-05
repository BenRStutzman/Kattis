import sys

def exp(probs):
    subs = len(probs)-1
    t = 0
    for i in range(1,len(probs)):
        t += i**(i/subs)*probs[i]
    return t

def update(probs, new):
    newprobs = [0]
    for p in probs:
        newprobs[-1] += p*(1-new)
        newprobs.append(p*new)
    return newprobs

def main():
    inp = sys.stdin.readlines()
    papers = sorted((int(p) for p in inp[1].split()), key = lambda x: -x)
    probs = [1]
    best = 0
    for paper in papers:
        probs = update(probs, paper/100)
        index = exp(probs)
        if best < index:
            best = index
    print(best)



main()
