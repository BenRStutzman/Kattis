import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N = inp[0][0]
    values = [0 for i in range(2 * 10 ** 6 + 1)]

    exp_val = 1
    last_start = inp[-1][0]

    for start, first_end, last_end in inp[N:0:-1]:
        first_end = start + first_end
        last_end = start + last_end

        for hour in range(start + 1, last_start + 1):
            values[hour] = exp_val

        end_length = last_end - first_end + 1
        exp_val = max(sum(values[first_end : last_end + 1])/ end_length + 1, exp_val)

        last_start = start

    print(exp_val)

main()
