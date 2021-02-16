def memoize(func):
    cache = {}

    def funcMem(*args):
        if not args in cache:
            cache[args] = func(*args)
        return cache[args]
    return funcMem


class Solution:
    def minDiffernce(self, a, n):
        s = sum(a)
        s2 = s//2 + 1
        dp = [[False] * (s2+1) for j in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, s2+1):
                if j < a[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-a[i-1]]

        diff = float('inf')
        for i in range(s2, -1, -1):
            if dp[n][i]:
                diff = min(diff, abs(s - 2 * i))

        return diff

    # use memoization
    def minDiffernceV3(self, arr, n):
        def minDiff(i, sum, sumTotal):
            if i == 0:
                return abs(sumTotal - sum - sum)
            else:
                return min(
                    minDiff(i - 1, sum + arr[i-1], sumTotal),
                    minDiff(i - 1, sum, sumTotal)
                )

        minDiff = memoize(minDiff)
        return minDiff(n, 0, sum(arr))

    # reduce number of args
    def minDiffernceV2(self, arr, n):
        def minDiff(arr, sum, sumTotal):
            if len(arr) == 0:
                return abs(sumTotal - sum - sum)
            else:
                return min(
                    minDiff(arr[1:], sum + arr[0], sumTotal),
                    minDiff(arr[1:], sum, sumTotal)
                )

        return minDiff(arr, 0, sum(arr))

    # simple
    def minDiffernceV1(self, arr, n):
        def minDiff(arr, i, sum, sumTotal):
            if i == 0:
                return abs(sumTotal - sum - sum)
            else:
                return min(
                    minDiff(arr, i - 1, sum + arr[i-1], sumTotal),
                    minDiff(arr, i - 1, sum, sumTotal)
                )

        return minDiff(arr, n, 0, sum(arr))


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        input()
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minDiffernce(arr, N)
        print(ans)
