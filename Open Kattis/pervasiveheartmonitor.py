import sys

def main():
    inp = [line.split() for line in sys.stdin.readlines()]
    for line in inp:
        name = [section for section in line if section.isalpha()]
        beats = [float(section) for section in line if not section.isalpha()]
        print(sum(beats) / len(beats), ' '.join(name))

main()
