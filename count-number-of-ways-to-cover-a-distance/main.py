def memoize(func):
    cache = {}

    def funcMem(*args):
        if not args in cache:
            cache[args] = func(*args)
        return cache[args]
    return funcMem


def countWays(n):
    dp = [0] * (n+1)

    for i in range(n+1):
        if i == 0 or i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = dp[i-1] + dp[i-2] + 0
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n] % 1000000007


def countWaysV1(n):
    def counts(n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            return counts(n-1) + counts(n-2) + counts(n-3)

    counts = memoize(counts)
    return counts(n) % 1000000007


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        input()
        m = int(input())
        print(countWays(m))
