import math

def f(m, n, x):
    return math.ceil(m/x) + math.ceil(n/x) + x - 1

for _ in range(int(input())):
    m,n = map(int,input().split())
    left = 1
    right = math.ceil(math.sqrt(max(m,n)))
    while left < right:
        mid = (left + right) // 2
        midmid = (right + mid) // 2
        if f(m, n, mid) > f(m, n, midmid):
            left = mid
        else:
            right = midmid
    print(f(m, n, left))