def memoize(func):
    cache = {}

    def funcMem(*args):
        key = str(args)
        if not key in cache:
            cache[key] = func(*args)
        return cache[key]
    return funcMem


def optimalStrategyOfGame(arr, n):
    def f(l, r, sum, dp):
        if l + 1 == r:
            return max(arr[l], arr[r])

        if dp[l][r] != -1:
            return dp[l][r]

        dp[l][r] = max(
            sum - f(l+1, r, sum-arr[l], dp),
            sum - f(l, r-1, sum-arr[r], dp)
        )
        return dp[l][r]

    l = 0
    r = n - 1
    sm = sum(arr)
    dp = [[-1] * (n) for _ in range(n)]
    res = f(l, r, sm, dp)
    return res


def optimalStrategyOfGameV2(arr, n):
    def f(l, r, sum):
        if l + 1 == r:
            return max(arr[l], arr[r])

        return max(
            sum - f(l+1, r, sum-arr[l]),
            sum - f(l, r-1, sum-arr[r])
        )

    l = 0
    r = n - 1
    sm = sum(arr)
    f = memoize(f)
    res = f(l, r, sm)
    return res


def optimalStrategyOfGameV1(arr, n):
    def f(l, r, player, sum1, sum2):
        if r < l:
            return sum1, sum2

        player = not player

        if player:
            s1, s2 = f(l+1, r, player, sum1 + arr[l], sum2)
            c1, c2 = f(l, r-1, player, sum1 + arr[r], sum2)
            return (s1, s2) if s1 > c1 else (c1, c2)
        else:
            s1, s2 = f(l+1, r, player, sum1, sum2 + arr[l])
            c1, c2 = f(l, r-1, player, sum1, sum2 + arr[r])
            return (s1, s2) if s2 > c2 else (c1, c2)

    l = 0
    r = len(arr) - 1
    player = False
    sum1 = 0
    sum2 = 0
    f = memoize(f)
    s1, _ = f(l, r, player, sum1, sum2)
    return s1


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        input()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(optimalStrategyOfGame(arr, n))
