import sys

def new_exps(num):
    factors = []

    while not num % 2:
        factors.append(2)
        num //= 2

    factor = 3

    while factor ** 2 <= num:
        if num % factor:
            factor += 2
        else:
            factors.append(factor)
            num //= factor
    if num > 1:
        factors.append(num)
        
    factors = sorted([factors.count(factor) for factor in set(factors)])
    if len(factors) > 2:
        return False
    else:
        return factors
        
def main():
    
    inp = [line.split() for line in sys.stdin.read().splitlines()]

    names = ["Alice", "Bob"]

    results = ''
    
    for game in inp[1:]:

        N = int(game[0])
        
        factorization = new_exps(N)

        if factorization:
            winner = -1
            first_name = game[1]
            if len(factorization) == 1:
                winner = (factorization[0] + 1) % 2
            else:
                if factorization[0] == factorization[1]:
                    winner = 1
                elif factorization[1] - factorization[0] == 1:
                    winner = 0
                else:
                    winner_name = "tie"
            if winner == 0:
                winner_name = first_name
            elif winner == 1:
                winner_name = names[(names.index(first_name) + 1) % 2] 
        else:
            winner_name = "tie"

        results += winner_name + '\n'

    print results[:-1]
    
main()
