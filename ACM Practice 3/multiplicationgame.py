import sys
from time import time

def prime_fact_exps(num):
    factors = []
    
    num_this_factor = 0
    while num % 2 == 0:
        num_this_factor += 1
        num //= 2
    if num_this_factor:
        factors.append(num_this_factor)
    
    factor = 3
    while num > 1:
        if factor ** 2 > num:
            factors.append(1)
            if len(factors) > 2:
                return False
            break
        if num % factor == 0:
            num_this_factor = 0
            while num % factor == 0:
                num_this_factor += 1
                num //= factor
            factors.append(num_this_factor)
            if len(factors) > 2:
                return False
        factor += 2 if ((factor + 2) % 3) else 4
    return sorted(factors, reverse = True)

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

    total_start_time = time()
    time1 = 0
    time2 = 0
    time3 = 0
    
    inp = [line.split() for line in sys.stdin.read().splitlines()]

    names = ["Alice", "Bob"]

    results = ''
    
    for game in inp[1:]:
        start_time = time()

        N = int(game[0])

        time1 += time() - start_time
        start_time = time()
        
        factorization = new_exps(N)

        time2 += time() - start_time
        start_time = time()

        #print(N, factorization)

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


        time3 += time() - start_time
        start_time = time()
        #print(prime_fact_exps(N))

    print(results[:-1])
    print("time1:", time1)
    print("time2:", time2)
    print("time3:", time3)
    print("total_time:", time() - total_start_time)
    
main()
