from collections import defaultdict

def prime_factorize(n):
    factors = defaultdict(int)
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] += 1
    if n > 1:
        factors[n] += 1
    return factors

def count_prime_factors(array):
    result = defaultdict(int)
    for num in array:
        factors = prime_factorize(num)
        for factor, count in factors.items():
            result[factor] += count
    return result

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        dict = count_prime_factors(a)
        count = 0
        temp = 0
        for k in dict:
            count += dict[k]//2
            temp += dict[k] % 2
            if temp == 3:
                count += 1
                temp = 0
        print(count)

if __name__ == "__main__":
    main()