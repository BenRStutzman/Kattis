import sys

def main():

    answers = sys.stdin.read().splitlines()[1]

    Adrian = "ABC"
    Bruno = "BABC"
    Goran = "CCAABB"
    A_score = 0
    B_score = 0
    G_score = 0

    for index, char in enumerate(answers):
        if char == Adrian[index % 3]:
            A_score += 1
        if char == Bruno[index % 4]:
            B_score += 1
        if char == Goran[index % 6]:
            G_score += 1

    high_score = max(A_score, B_score, G_score)

    print(high_score)
    if A_score == high_score:
        print("Adrian")
    if B_score == high_score:
        print("Bruno")
    if G_score == high_score:
        print("Goran")

main()
