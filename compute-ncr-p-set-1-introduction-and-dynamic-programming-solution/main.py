import sys
MOD = pow(10, 9)+7


def memoize(func):
    cache = {}

    def funcMem(*args):
        if not args in cache:
            cache[args] = func(*args)
        return cache[args]
    return funcMem


def nCrV1(n, r):
    def factorial(n):
        if n <= 0:
            return 1
        return n*factorial(n-1)

    c = factorial(n) // (factorial(r) * factorial(n - r))
    return c % MOD


# Time Limit Exceeded
def nCrV2(n, r):
    def f(n, k):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return f(n-1, k-1) + f(n-1, k)

    f = memoize(f)
    return f(n, r) % MOD


def nCrV3(N, K):
    C = [[0 for x in range(K+1)] for x in range(N+1)]

    for n in range(N+1):
        for k in range(min(n, K)+1):
            if k == 0 or k == n:
                C[n][k] = 1
            else:
                C[n][k] = C[n-1][k-1] + C[n-1][k]

    return C[N][K] % MOD


sys.setrecursionlimit(10000)


class Solution:
    def nCr(self, n, r):
        return nCrV1(n, r)
        # return nCrV2(n, r)
        # return nCrV3(n, r)

# ----------------------------


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        n, r = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.nCr(n, r))
