for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1.sort()
    arr2.sort()
    res = 1
    pointer1 = 0
    pointer2 = 0
    while pointer1 < n and pointer2 < n:
        if arr1[pointer1] <= arr2[pointer2]:
            res *= (pointer2-pointer1)
            res = res % (10**9+7)
            if res <= 0:
                break
            pointer1 += 1
        else:
            pointer2 += 1
    while pointer1 < pointer2:
        res *= (pointer2-pointer1)
        res = res % (10**9+7)
        pointer1 += 1
    print(res)