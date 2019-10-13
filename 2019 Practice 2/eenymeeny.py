import sys

def main():
    inp = sys.stdin.read().splitlines()
    n_words = len(inp[0].split())
    n_people = int(inp[1])
    people = inp[2:]
    teams = [[], []]
    for i in range(n_people):
        index = (n_words - 1) % len(people)
        #print(index)
        teams[i % 2].append(people[index])
        people = people[index + 1:] + people[:index]
        #print(people)
    for team in teams:
        print(len(team))
        for person in team:
            print(person)

main()
