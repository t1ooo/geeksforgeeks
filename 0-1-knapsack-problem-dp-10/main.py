def memoize(func):
    cache = {}
    def funcMem(*args):
        if not args in cache:
            cache[args] = func(*args)
        return cache[args]
    return funcMem


# dynamic programming
def knapSack(maxWeight, weights, values, N):
    dp = [[0] * (maxWeight+1) for _ in range(N)]

    for i in range(N):
        for weight in range(maxWeight+1):
            if weight == 0:
                dp[i][weight] = 0
            elif weight < weights[i]:
                dp[i][weight] = dp[i-1][weight]
            else:
                dp[i][weight] = max(
                    dp[i-1][weight-weights[i]] + values[i],
                    dp[i-1][weight]
                )

    return dp[N-1][maxWeight]


# recursion + dynamic programming
def knapSackV2(maxWeight, weights, values, n):
    def f(i, weight, dp):
        if i < 0 or weight <= 0:
            return 0

        if dp[i][weight] != -1:
            return dp[i][weight]

        if weight < weights[i]:
            dp[i][weight] = f(i-1, weight, dp)
            return dp[i][weight]

        dp[i][weight] = max(
            f(i-1, weight-weights[i], dp) + values[i],
            f(i-1, weight, dp)
        )
        return dp[i][weight]

    dp = [[-1] * (maxWeight+1) for _ in range(n)]
    return f(n-1, maxWeight, dp)


# recursion + memoize
def knapSackV1(maxWeight, weights, values, n):
    def f(i, weight):
        if i < 0 or weight <= 0:
            return 0

        if weight < weights[i]:
            return f(i-1, weight)

        return max(
            f(i-1, weight-weights[i]) + values[i],
            f(i-1, weight)
        )

    f = memoize(f)
    return f(n-1, maxWeight)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        input()
        n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        print(knapSack(W, wt, val, n))
