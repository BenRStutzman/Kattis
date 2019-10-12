import sys

def main():
    inp = sys.stdin.read().splitlines()
    n_words = len(inp[0].split())
    n_people = int(inp[1])
    people = inp[2:]
    teams = [[], []]
    n = 0
    x = 0
    for i in range(n_people):
        x = (x - 1 + n_words) % len(people)
        person = people[x]
        teams[i % 2].append(person)
        people.remove(person)
    for team in teams:
        print(len(team))
        for person in team:
            print(person)
            
main()
            
