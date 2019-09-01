def main():

    a, b, c = [int(num) for num in input().split()]
    if a + b == c:
        print("%i+%i=%i" % (a, b, c))
    elif a - b == c:
        print("%i-%i=%i" % (a, b, c))
    elif a * b == c:
        print("%i*%i=%i" % (a, b, c))
    elif a / b == c:
        print("%i/%i=%i" % (a, b, c))
    elif a == b - c:
        print("%i=%i-%i" % (a, b, c))
    elif a == b / c:
        print("%i=%i/%i" % (a, b, c))
    
main()
