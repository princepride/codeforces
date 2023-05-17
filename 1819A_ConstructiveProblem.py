
def find_missing_number(arr):
    # 将数组转换为集合
    num_set = set(arr)

    # 从1开始逐个增加数字，检查是否在集合中出现
    num = 0
    while num in num_set:
        num += 1

    return num

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    m = find_missing_number(arr)
    #print('m '+str(m))

    min_index = -1
    max_index = -1
    for index, num in enumerate(arr):
        if num == m + 1:
            if min_index == -1:
                min_index = index
            else:
                max_index = index
    #print('min_index '+str(min_index))
    #print('max_index '+str(max_index))
    if min_index == -1:
        print('no')
    elif max_index == -1:
        print('yes')
    else:
        for i in range(min_index,max_index+1):
            arr[i] = m
        if find_missing_number(arr) == m+1:
            print('yes')
        else:
            print('no')

