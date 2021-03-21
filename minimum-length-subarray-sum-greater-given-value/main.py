# Time Limit Exceeded
def smallestSubarrayV1(arr, n, x):
    for ln in range(1, n+1):
        for i in range(n-ln+1):
            tmp = arr[i:i+ln]
            # print(tmp)
            if sum(tmp) > x:
                return ln

    return -1


# Time Limit Exceeded
def smallestSubarrayV2(arr, n, x):
    dp = [[0] * (n+1) for _ in range(n)]
    for ln in range(1, n+1):
        for l in range(n-ln+1):
            r = l+ln

            sm = 0
            if ln == 1:
                sm = arr[l]
            else:
                sm = dp[l][r-1] + arr[r-1]

            dp[l][r] = sm

            if sm > x:
                return ln

    return -1


# Time Limit Exceeded
def smallestSubarrayV3(arr, n, x):
    ln = n + 1
    for i in range(0, n):
        sm = arr[i]
        if sm > x:
            return 1

        for k in range(i+1, n):
            sm += arr[k]
            if sm > x:
                ln = min(ln, k-i+1)

    return ln


def smallestSubarrayV4(arr, n, x):
    sum = 0
    minLen = n + 1
    l, r = 0, 0
    while r < n:
        while sum <= x and r < n:
            sum += arr[r]
            r += 1

        while sum > x and l < n:
            minLen = min(minLen, r - l)
            sum -= arr[l]
            l += 1

    return minLen


class Solution:
    def sb(self, arr, n, x):
        # return smallestSubarrayV1(arr, n, x)
        # return smallestSubarrayV2(arr, n, x)
        # return smallestSubarrayV3(arr, n, x)
        return smallestSubarrayV4(arr, n, x)


# ---------------------------
if __name__ == "__main__":
    T = int(input())
    while(T > 0):
        input()
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().sb(a, n, m))
        T -= 1
