n = int(input())
store = []
check = 0
for i in range(n):
    a, b = map(int, input().split())
    store.append([b-a, i])
    check += (b-a)
 
store.sort()
 
vals = [i[0] for i in store]
if len(vals) > 1:
    fir =abs(-1 * vals[0] + sum(vals[1:]))
    sec = abs(sum(vals[:-1]) + -1 * vals[-1])
    mx = max(fir, sec, check)
 
    if mx == fir:
        print(store[0][1] + 1 )
    elif mx == sec:
        print(store[-1][1] + 1)
    else:
        print(0)
else:
    print(0)