import sys

def main():
    inp = sys.stdin.read().splitlines()
    for case in inp[1:]:
        coords = [int(num) for num in case.split()]
        rects = sorted([[coords[i], coords[i + 1]] for i in range(0, len(coords), 2)], key = max)
        A = sorted(rects[2])
        #print(A[1])
        B, C = rects[0], rects[1]
        #print(B, C)
        try_1 = max(A[1], B[0] + C[0]) * (A[0] + max(B[1], C[1]))
        try_2 = max(A[1], B[0] + C[1]) * (A[0] + max(B[1], C[0]))
        try_3 = max(A[1], B[1] + C[0]) * (A[0] + max(B[0], C[1]))
        try_4 = max(A[1], B[1] + C[1]) * (A[0] + max(B[0], C[0]))
        try_5 = max(A[1], B[0], C[0]) * (A[0] + B[1] + C[1])
        try_6 = max(A[1], B[0], C[1]) * (A[0] + B[1] + C[0])
        try_7 = max(A[1], B[1], C[0]) * (A[0] + B[0] + C[1])
        try_8 = max(A[1], B[1], C[1]) * (A[0] + B[0] + C[0])
        way_1 = min(try_1, try_2, try_3, try_4, try_5, try_6, try_7, try_8)
        
        A = sorted(rects[0])
        #print(A[1])
        B, C = rects[1], rects[2]
        #print(B, C)
        try_1 = max(A[1], B[0] + C[0]) * (A[0] + max(B[1], C[1]))
        try_2 = max(A[1], B[0] + C[1]) * (A[0] + max(B[1], C[0]))
        try_3 = max(A[1], B[1] + C[0]) * (A[0] + max(B[0], C[1]))
        try_4 = max(A[1], B[1] + C[1]) * (A[0] + max(B[0], C[0]))
        way_2 = min(try_1, try_2, try_3, try_4)

        A = sorted(rects[1])
        #print(A[1])
        B, C = rects[0], rects[2]
        #print(B, C)
        try_1 = max(A[1], B[0] + C[0]) * (A[0] + max(B[1], C[1]))
        try_2 = max(A[1], B[0] + C[1]) * (A[0] + max(B[1], C[0]))
        try_3 = max(A[1], B[1] + C[0]) * (A[0] + max(B[0], C[1]))
        try_4 = max(A[1], B[1] + C[1]) * (A[0] + max(B[0], C[0]))
        way_3 = min(try_1, try_2, try_3, try_4)

        A = sorted(rects[2], reverse = True)
        #print(A[1])
        B, C = rects[0], rects[1]
        #print(B, C)
        try_1 = max(A[1], B[0] + C[0]) * (A[0] + max(B[1], C[1]))
        try_2 = max(A[1], B[0] + C[1]) * (A[0] + max(B[1], C[0]))
        try_3 = max(A[1], B[1] + C[0]) * (A[0] + max(B[0], C[1]))
        try_4 = max(A[1], B[1] + C[1]) * (A[0] + max(B[0], C[0]))
        try_5 = max(A[1], B[0], C[0]) * (A[0] + B[1] + C[1])
        try_6 = max(A[1], B[0], C[1]) * (A[0] + B[1] + C[0])
        try_7 = max(A[1], B[1], C[0]) * (A[0] + B[0] + C[1])
        try_8 = max(A[1], B[1], C[1]) * (A[0] + B[0] + C[0])
        way_4 = min(try_1, try_2, try_3, try_4, try_5, try_6, try_7, try_8)
        
        A = sorted(rects[0], reverse = True)
        #print(A[1])
        B, C = rects[1], rects[2]
        #print(B, C)
        try_1 = max(A[1], B[0] + C[0]) * (A[0] + max(B[1], C[1]))
        try_2 = max(A[1], B[0] + C[1]) * (A[0] + max(B[1], C[0]))
        try_3 = max(A[1], B[1] + C[0]) * (A[0] + max(B[0], C[1]))
        try_4 = max(A[1], B[1] + C[1]) * (A[0] + max(B[0], C[0]))
        way_5 = min(try_1, try_2, try_3, try_4)

        A = sorted(rects[1], reverse = True)
        #print(A[1])
        B, C = rects[0], rects[2]
        #print(B, C)
        try_1 = max(A[1], B[0] + C[0]) * (A[0] + max(B[1], C[1]))
        try_2 = max(A[1], B[0] + C[1]) * (A[0] + max(B[1], C[0]))
        try_3 = max(A[1], B[1] + C[0]) * (A[0] + max(B[0], C[1]))
        try_4 = max(A[1], B[1] + C[1]) * (A[0] + max(B[0], C[0]))
        way_6 = min(try_1, try_2, try_3, try_4)

        print(min(way_1, way_2, way_3, way_4, way_5, way_6))
        
main()
