import sys, math

def main():
    inp = sys.stdin.readlines()
    P, D = inp[0].split()
    districts = {}
    for i in range(1,int(D)+1):
        districts[str(i)]=[0,0]
    for pre in inp[1:]:
        D, A, B = pre.split()
        districts[D][0] += int(A)
        districts[D][1] += int(B)
    AW, BW, T = 0, 0, 0
    for d in districts:
        dt = sum(districts[d])
        T += dt
        winner = 1
        if districts[d][0] > districts[d][1]:
            winner = 0
        wasted = (districts[d][1-winner], districts[d][winner]-math.floor(dt/2+1))
        AW += wasted[1-winner]
        BW += wasted[winner]
        print("AB"[winner], wasted[1-winner], wasted[winner])
    print(abs(AW-BW)/T)
    
        
main()
