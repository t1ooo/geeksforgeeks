def equalPartition(N, arr):
    sm = sum(arr)
    if sm % 2 == 1:
        return False

    sm = sm//2
    dp = [[False] * (sm + 1) for i in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = True

    for i in range(1, sm + 1):
        dp[0][i] = False

    for i in range(1, N + 1):
        for j in range(1, sm + 1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

    return dp[N][sm]


def equalPartitionV3(N, arr):
    s = sum(arr)
    if s % 2 == 1:
        return 0

    s = s//2
    dp = {0}
    for v in arr:
        dp.update({x+v for x in dp})
        if s in dp:
            return True

    return False


def equalPartitionV2(N, arr):
    def minDiff(arr, n, sum, totalSum, dp):
        if dp[n][sum] != -1:
            return dp[n][sum]

        if n == 0:
            dp[n][sum] = abs(totalSum - sum - sum)
            return dp[n][sum]

        dp[n][sum] = min(
            minDiff(arr, n-1, sum, totalSum, dp),
            minDiff(arr, n-1, sum + arr[n-1], totalSum, dp)
        )
        return dp[n][sum]

    dp = [[-1] * (sum(arr) + 1) for i in range(N + 1)]
    diff = minDiff(arr, N, 0, sum(arr), dp)
    return diff == 0


# def equalPartitionV2(N, arr):
#     def minDiff(arr, n, sum, totalSum, dp):
#         if dp[n] != -1:
#             return dp[n]

#         if n == 0:
#             dp[n] = abs(totalSum - sum - sum)
#             return dp[n]

#         dp[n] = min(
#             minDiff(arr, n-1, sum, totalSum, dp[0:]),
#             minDiff(arr, n-1, sum + arr[n-1], totalSum, dp[0:])
#         )
#         return dp[n]

#     dp = [-1] * (N+1)
#     diff = minDiff(arr, N, 0, sum(arr), dp)
#     return diff == 0


def equalPartitionV1(N, arr):
    def minDiff(arr, n, sum, totalSum):
        if n == 0:
            return abs(totalSum - sum - sum)

        return min(
            minDiff(arr, n-1, sum, totalSum),
            minDiff(arr, n-1, sum + arr[n-1], totalSum)
        )

    return 0 == minDiff(arr, len(arr), 0, sum(arr))


class Solution:
    def equalPartition(self, N, arr):
        return equalPartition(N, arr)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])

        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
