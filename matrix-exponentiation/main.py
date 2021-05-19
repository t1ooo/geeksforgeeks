# Time Limit Exceeded
def genFibNumV1(a, b, c, n, m):
    def G(n):
        if n == 1 or n == 2:
            return 1
        return a*G(n-1) + b*G(n-2) + c

    return G(n) % m


# Time Limit Exceeded
def genFibNumV2(a, b, c, n, m):
    if n <= 2:
        return 1 % m

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        dp[i] = (a*dp[i-1] + b*dp[i-2] + c) % m

    return dp[n]


def multiply(a, b):
    mul = [[0 for x in range(3)]
           for y in range(3)]

    for i in range(3):
        for j in range(3):
            mul[i][j] = 0
            for k in range(3):
                mul[i][j] += a[i][k] * b[k][j]

    for i in range(3):
        for j in range(3):
            a[i][j] = mul[i][j]


def power(F, n, a, b, c):
    M = [[a, b, 1], [1, 0, 0], [0, 0, 1]]
    if (n == 1):
        return F[0][0] + F[0][1] + c

    power(F, int(n / 2), a, b, c)

    multiply(F, F)

    if (n % 2 != 0):
        multiply(F, M)

    return F[0][0] + F[0][1] + c


def genFibNumV3(a, b, c, n, m):
    F = [[a, b, 1], [1, 0, 0], [0, 0, 1]]
    r = power(F, n-2, a, b, c) % m
    return r


class Solution:
    def genFibNum(self, a, b, c, n, m):
        # return genFibNumV1(a, b, c, n, m)
        # return genFibNumV2(a, b, c, n, m)
        return genFibNumV3(a, b, c, n, m)


# -------------------------------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        a, b, c, n, m = map(int, input().split())
        ob = Solution()
        print(ob.genFibNum(a, b, c, n, m))
