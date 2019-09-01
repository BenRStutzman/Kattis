import sys

def main():

    words = set()
    for word in input().split():
        if word in words:
            print("no")
            break
        else:
            words.add(word)
    else:
        print("yes")
        
main()
