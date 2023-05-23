class Index:
    def __init__(self, index, num) -> None:
        self.index = index
        self.num = num

for _ in range(int(input())):
    n, t1, t2 = map(int, input().split(' '))
    arrinput = list(map(int, input().split(' ')))
    arr=[]
    for i in range(n):
        arr.append(Index(i, arrinput[i]))
    arr.sort(key=lambda x: x.num, reverse=True)
    arr1=[]
    arr2=[]
    len1 = 1
    len2 = 1
    for i in range(n):
        if len1 * t1 <= len2 * t2:
            arr1.append(arr[i].index+1)
            len1 += 1
        else:
            arr2.append(arr[i].index+1)
            len2 += 1
    print(len(arr1), *arr1)
    print(len(arr2), *arr2)




