import sys

def main():
    inp = sys.stdin.read().splitlines()
    prompt = inp[0]
    n = int(inp[1])
    choices = inp[2:]
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    first_lets = {char: 0 for char in alpha}
    for choice in choices:
        first_lets[choice[0]] += 1
    good_choices = [choice for choice in choices if choice[0] == prompt[-1]]
    if good_choices:
        for choice in good_choices:
            first_lets[choice[0]] -= 1
            if first_lets[choice[-1]] <= 0:
                print(choice + "!")
                break
            first_lets[choice[0]] += 1
        else:
            print(good_choices[0])
    else:
        print("?")

main()
