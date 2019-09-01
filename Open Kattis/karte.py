def main():
    cards = {'P': set(), 'K': set(), 'H': set(), 'T': set()}
    inp = input()

    for i in range(0,len(inp),3):
        card = inp[i:i + 3]
        if card in cards[card[0]]:
            print("GRESKA")
            return
        cards[card[0]].add(card)

    print(13 - len(cards['P']), 13 - len(cards['K']), 13 - len(cards['H']), 13 - len(cards['T']))
    

main()
