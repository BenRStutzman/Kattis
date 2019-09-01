def main():
    
    string = input()
    lower = 0
    upper = 0
    white = 0
    symbol = 0
    
    for char in string:
        if char == '_':
            white += 1
        elif char.isalpha():
            if char.isupper():
                upper += 1
            else:
                lower += 1
        else:
            symbol += 1

    L = len(string)
    print(white / L)
    print(lower / L)
    print(upper / L)
    print(symbol / L)        
        
main()
