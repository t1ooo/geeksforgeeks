MOD = pow(10, 9)+7


class Solution:
    def numOfSubsets(self, arr, N):
        def f(n):
            return pow(2, n)-1

        maxCount = arr.count(max(arr))
        minCount = arr.count(min(arr))

        return f(maxCount) % MOD, f(minCount) % MOD


# --------------------------

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        Arr = list(map(int, input().split()))
        ob = Solution()
        ptr = ob.numOfSubsets(Arr, N)
        print(*ptr)
