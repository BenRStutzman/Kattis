import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N = inp[0][0]
    values = [[inp[N][0] + 1, 0]]

    last_start = inp[N][0] + 1
    last_exp_val = 0

    for start, first_end, last_end in inp[N:0:-1]:
        #print("------------------------------")
        first_end = start + first_end
        last_end = start + last_end
        #print("start:", start)
        #print("first_end:", first_end)
        #print("last_end:", last_end)
        if last_start != start:
            values.append([start, last_exp_val])
        #print("values:", values)
        total = 0
        last_time = first_end - 1
        for time, exp_val in values[::-1]:
            #print("----------")
            #print("time:", time)
            #print("exp_val:", exp_val)
            if time > last_end:
                break
            if time >= first_end:
                #print("adding:", exp_val, '*', time, '-', last_time)
                total += exp_val * (time - last_time)
                last_time = time
        #print("total:", total)
        total += exp_val * (last_end - last_time )
        #print("total:", total)
            
        end_length = last_end - first_end + 1
        #print("end_length:", end_length)
        new_exp_val = total / end_length + 1
        #print("new_exp_val:", new_exp_val)
        #print("old values:", values)
        if new_exp_val > last_exp_val:
            exp_val = new_exp_val
            last_exp_val = new_exp_val
            values[-1][1] = new_exp_val
        elif last_start != start:
            values.remove([start, last_exp_val])
        last_start = start
        #print("new values:", values)
    print(values[-1][1])

main()
