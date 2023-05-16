def fun(n):
    return n*(n-1)/2

for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    hasFind = False
    for i in range(n+1):
        if k == fun(i) + fun(n-i):
            print('Yes')
            hasFind = True
            a = [1 for _ in range(i)] + [-1 for _ in range(n-i)]
            print(*a)
            break
    if not hasFind:
        print('No')