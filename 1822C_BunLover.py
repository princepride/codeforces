# F(n) = F(n-1) + 2n + 1
# F(4) = 26
# F(n) - F(n-1) = 2n + 1
# F(5) - F(4) = 11 = 2*5 + 1
# F(n) - F(4) = 1*(n-4) + (5+n)*(n-4)
#F(n) = 26+(n+6)*(n-4)

n = int(input().strip())
for _ in range(n):
    t = int(input().strip())
    print(26+(t+6)*(t-4))