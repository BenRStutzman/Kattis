[X, Y, N] = [int(num) for num in input().split()]

for i in range(1, N + 1):
    if i % X and i % Y:
        print(i)
    else:
        if not i % X:
            print('Fizz', end = '')
        if not i % Y:
            print('Buzz', end = '')
        print()
