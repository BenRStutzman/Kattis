import sys

def main():
    inp = sys.stdin.read().splitlines()
    prompt = inp[0]
    n = int(inp[1])
    choices = inp[2:]
    good_choices = []
    for choice in choices:
        if choice[0] == prompt[-1]:
            good_choices.append(choice)
    if good_choices:
        for option in good_choices:
            left = choices[:]
            left.remove(option)
            #print(left)
            for choice in left:
                #print("left:", choice)
                if choice[0] == option[-1]:
                    break
            else:
                print(option + "!")
                break
        else:
            print(good_choices[0])
    else:
        print("?")

main()
