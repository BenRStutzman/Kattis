from sys import stdin

def main():
    s, p = [int(num) for num in stdin.readline().split()]
    players = [[2, i] for i in range(1, p + 1)]
    counter = -1
    while len(players) > 1:
        #print("players:", players)
        counter = (counter + s) % len(players)
        #print("person:", players[counter])
        if players[counter][0] == 2:
            players[counter][0] = 1
            players.insert(counter + 1, players[counter].copy())
            counter -= 1
        elif players[counter][0] == 1:
            players[counter][0] = 0
        else:
            del players[counter]
            counter -= 1
    print(players[0][1])
    

main()
