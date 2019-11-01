import sys

def isprime(n):
    if (n<=1):
        return False
    if (n<=3):
        return True
    if (not(n%2) or not(n%3)):
        return False
    i=5
    while(i*i<=n):
        if (not(n%i) or not(n%(i+2))):
            return False
        i += 6
    return True

def main():
    inp = sys.stdin.read().splitlines()
    q = int(inp[0])
    numbs = [int(numb) for numb in inp[1:]]
    #print(numbs)
    for numb in numbs:
        facts = 0
        pfacts = 0
        r = [i for i in range(1,int(numb/2)+1)]
        r.append(numb)
        for f in r:
            if (numb/f%1==0.0):
                #print(f)
                facts += 1
                if (isprime(f)):
                    #print(f)
                    pfacts += 1
        print(facts-pfacts)
    
main()
