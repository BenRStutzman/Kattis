def main():
    quadkey = input().strip()
    N = len(quadkey)
    print(N, end = ' ')
    N -= 1
    x, y = 0, 0
    for char in quadkey:
        if char == '1' or char == '3':
            x += 2 ** N
        if char == '2' or char == '3':
            y += 2 ** N
        N -= 1

    print(x, y)
    
main()
