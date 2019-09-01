T = int(input())

for i in range(T):
    N = int(input())

    cities = set()
    
    for i in range(N):
        cities.add(input())

    print(len(cities))
