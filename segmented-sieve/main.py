import math

MOD = pow(10, 9)+7


def product(arr):
    res = 1
    for v in arr:
        res *= v
    return res


def sieve(n):
    nums = [True for x in range(n+1)]
    nums[0] = False
    nums[1] = False

    p = 2
    while p*p <= n:
        if nums[p]:
            for i in range(p*p, n+1, p):
                nums[i] = False
        p += 1

    primes = []
    for i in range(2, n+1):
        if nums[i]:
            primes.append(i)

    return primes


def segmentedSieve(lo, hi, primes):
    nums = [True for _ in range(lo, hi+1)]

    for p in primes:
        if p*p > hi:
            break
        start = max(p*p, lo + (p - lo % p) % p)
        for i in range(start, hi+1, p):
            nums[i-lo] = False

    res = []
    for i in range(lo, hi+1):
        if nums[i-lo]:
            res.append(i)

    return res


def primeProductV1(L, R):
    return product(segmentedSieve(L, R, PRIMES)) % MOD


def primeProductV2(L, R):
    limit = int(math.sqrt(R - L + 1) + 1)
    lo = L
    hi = lo + limit
    res = 1
    while lo <= R:
        hi = min(hi, R)
        res *= product(segmentedSieve(lo, hi, PRIMES))
        lo += limit+1
        hi = lo + limit

    return res % MOD


PRIMES = sieve(10000)


class Solution:
    def primeProduct(self, L, R):
        return primeProductV1(L, R)
        # return primeProductV2(L, R)

# -------------------------


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        L, R = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.primeProduct(L, R))
