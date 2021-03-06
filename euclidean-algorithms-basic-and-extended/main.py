def gcdV1(n, arr):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    res = arr[0]
    for i in range(1, len(arr)):
        res = gcd(res, arr[i])

    return res


def gcdV2(n, arr):
    def gcd(x, y):
        if x == 0:
            return y
        return gcd(y % x, x)

    from functools import reduce
    return reduce(gcd, arr)


class Solution:
    def gcd(self, n, arr):
        # return gcdV1(n, arr)
        return gcdV2(n, arr)

# --------------------------


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(n, arr))
