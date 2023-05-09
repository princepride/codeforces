for _ in range(int(input())):
    n=int(input())
    if n%2 and n>1: print(-1);continue
    a=[i for i in range(n)]
    for i in range(1,n,2): 
        a[i]=n-i
    a[0]=n
    print(*a)