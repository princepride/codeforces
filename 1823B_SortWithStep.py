def can_sort_permutation(test_cases):
    results = []
    
    for n, k, p in test_cases:
        sorted_indices = sorted(range(n), key=lambda x: p[x])
        possible = True
        for i in range(n):
            if (sorted_indices[i] - i) % k != 0:
                possible = False
                break

        if possible:
            results.append(0)
        else:
            preliminary_exchange = False
            for i in range(n - 1):
                if p[i] > p[i + 1]:
                    p[i], p[i + 1] = p[i + 1], p[i]
                    preliminary_exchange = True
                    break
            sorted_indices = sorted(range(n), key=lambda x: p[x])
            possible = True
            for i in range(n):
                if (sorted_indices[i] - i) % k != 0:
                    possible = False
                    break
                    
            if possible:
                results.append(1 if preliminary_exchange else 0)
            else:
                results.append(-1)

    return results

# Example usage:
#t = 6
#test_cases = [
#    (4, 1, [3, 1, 2, 4]),
#    (4, 2, [3, 4, 1, 2]),
#    (4, 2, [3, 1, 4, 2]),
#    (10, 3, [4, 5, 9, 1, 8, 6, 10, 2, 3, 7]),
#    (10, 3, [4, 6, 9, 1, 8, 5, 10, 2, 3, 7]),
#    (10, 3, [4, 6, 9, 1, 8, 5, 10, 3, 2, 7]),
#]

n = input()
test_cases = []
for i in range(int(n)):
    t = [int(num) for num in input().split(' ')]
    temp = [int(num) for num in input().split(' ')]
    t.append(temp)
    test_cases.append(tuple(t))

print(*can_sort_permutation(test_cases))