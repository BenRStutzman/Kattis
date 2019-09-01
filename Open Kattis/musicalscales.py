import sys

def main():
    notes = sys.stdin.read().splitlines()[1].split()
    works = []

    chromatic = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    for index, start_note in enumerate(chromatic):
        scale = [start_note]
        i = index
        for step in [2, 2, 1, 2, 2, 2, 1]:
            i += step
            i %= 12
            scale.append(chromatic[i])
        for note in notes:
            if note not in scale:
                break
        else:
            works.append(start_note)

    if works:
        print(' '.join(works))
    else:
        print("none")
    
main()
