for _ in range(int(input())):
    n, m = map(int, input().split())
    while m != 0 and m != 1:
        m = n % m
    if m == 0:
        print("NO")
    else:
        print("YES")