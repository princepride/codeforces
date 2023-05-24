for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    # get the max two num and min two num in arr
    max1 = max2 = float('-inf')  # Initialize max1 and max2 with negative infinity
    min1 = min2 = float('inf')
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    print(max(max1*max2, min1*min2))
