while True:
    num = input()

    if num == '0':
        break

    sum_dig = sum([int(char) for char in num])
    p = 11
    
    while True:
        new_num = str(int(num) * p)
        if sum([int(char) for char in new_num]) == sum_dig:
            print(p)
            break
        p += 1
