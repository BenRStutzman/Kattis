import sys

def ballpark(freq, keys):
    for i in range(1, 11):
        if freq < keys[0][i]:
            return i - 1

def find_note(freq, keys, names):
    ball = ballpark(freq, keys)
    if abs(freq - keys[0][ball]) <= 10 ** -4 or abs(freq - keys[0][ball + 1]) <= 10 ** -4:
        return 'A'
    for index, freqs in enumerate(keys[1:]):
        if abs(freq - freqs[ball]) <= 10 ** -4:
            return names[index]
    return "ERROR"

def main():
    keys = []
    names = ['Bb', 'B', 'C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab']

    groups = {'G major': {'G', 'A', 'B', 'C', 'D', 'E', 'F#'},
              'C major': {'C', 'D', 'E', 'F', 'G', 'A', 'B'},
              'Eb major': {'Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'},
              'F# minor': {'F#', 'Ab', 'A', 'B', 'C#', 'D', 'E'},
              'G minor': {'G', 'A', 'Bb', 'C', 'D', 'Eb', 'F'}}
    
    base = 440
    for i in range(12):
        group = [base * (2 ** i) for i in range(-6, 5)]
        keys.append(group)
        base *= (2 ** (1 / 12))
    #print(keys)
    notes = []
    inp = [float(num) for num in sys.stdin.read().splitlines()[1:]]
    for freq in inp:
        notes.append(find_note(freq, keys, names))
    notes_set = set(notes)
    possibles = []
    for name, group in groups.items():
        if not notes_set.difference(group):
            possibles.append(name)
    if len(possibles) == 1:
        print(possibles[0])
        if possibles[0] == 'F# minor':
            for note in notes:
                if note == 'Ab':
                    print('G#')
                else:
                    print(note)
        else:
            for note in notes:
                print(note)
    else:
        print('cannot determine key')
    


main()
