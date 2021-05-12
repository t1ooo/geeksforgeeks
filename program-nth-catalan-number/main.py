import functools


@functools.lru_cache()
def findCatalanV1(n):
    if n <= 1:
        return 1
    else:
        return sum(findCatalanV1(i) * findCatalanV1(n-i-1) for i in range(n))


# dynamic programming
def findCatalanV2(n):
    if n <= 1:
        return 1

    d = [0] * (n+1)
    d[0] = 1
    d[1] = 1

    for i in range(2, n+1):
        for j in range(i):
            d[i] += d[j] * d[i-j-1]

    return d[n]


# using binomial coefficient
def findCatalanV3(n):
    def binomialCoefficient(n, k):
        if k > n - k:
            k = n - k

        res = 1
        for i in range(k):
            res = res * (n-i)
            res = res // (i+1)

        return res

    return binomialCoefficient(2*n, n) // (n+1)


def findCatalanV4(n):
    res = 1
    for i in range(1, n+1):
        res *= (4*i)-2
        res //= i+1
    return res


class Solution:
    def findCatalan(self, n):
        # return findCatalanV1(n)
        # return findCatalanV2(n)
        # return findCatalanV3(n)
        return findCatalanV4(n)


# ---------------------------
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        input()
        n = int(input())
        print(Solution().findCatalan(n))
