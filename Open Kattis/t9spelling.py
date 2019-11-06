from sys import stdin

def press(char):
    if char in 'abc':
        return '2', 'abc'.index(char) + 1
    elif char in 'def':
        return '3', 'def'.index(char) + 1
    elif char in 'ghi':
        return '4', 'ghi'.index(char) + 1
    elif char in 'jkl':
        return '5', 'jkl'.index(char) + 1
    elif char in 'mno':
        return '6', 'mno'.index(char) + 1
    elif char in 'pqrs':
        return '7', 'pqrs'.index(char) + 1
    elif char in 'tuv':
        return '8', 'tuv'.index(char) + 1
    elif char in 'wxyz':
        return '9', 'wxyz'.index(char) + 1
    elif char == ' ':
        return '0', 1

def main():
    inp = [line[:-1] for line in stdin.readlines()]
    #print(inp)
    for i, line in enumerate(inp[1:]):
        to_print = ""
        last_key = 1
        for char in line:
            key, times = press(char)
            if key == last_key:
                to_print += " "
            to_print += key * times
            last_key = key
        print("Case #%d: %s" % (i + 1, to_print))

main()
        
