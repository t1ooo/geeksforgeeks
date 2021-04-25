def sqrtV1(n):
    return int(pow(n, 0.5))


def sqrtV2(n):
    if n == 0 or n == 1:
        return n

    i = 1
    res = 1
    while res <= n:
        i += 1
        res = i * i

    return i-1


def sqrtV3(n):
    if n == 0 or n == 1:
        return n

    res = 1
    l = 1
    r = n
    while l <= r:
        m = (l+r) // 2
        m2 = m * m

        if m2 == n:
            return m
        elif m2 < n:
            l = m + 1
            res = m
        else:
            r = m - 1

    return res


# Time Limit Exceeded
def countSquaresV1(N):
    def isPerfectSquare(n):
        root = sqrtV1(n)
        return n == root * root

    count = 0
    for n in range(1, N):
        if isPerfectSquare(n):
            count += 1

    return count


# Time Limit Exceeded
def countSquaresV2(N):
    count = 0
    n = 1
    while n * n < N:
        count += 1
        n += 1

    return count


def countSquaresV3(N):
    return sqrtV3(N-1)


class Solution:
    def countSquares(self, N):
        # return countSquaresV1(N)
        # return countSquaresV2(N)
        return countSquaresV3(N)


def testSqrt():
    import math

    for i in range(0, 10000):
        root = int(math.sqrt(i))
        assert sqrtV1(i) == root
        assert sqrtV2(i) == root
        assert sqrtV3(i) == root

# -----------------------


if __name__ == '__main__':
    testSqrt()
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        ob = Solution()
        print(ob.countSquares(N))
