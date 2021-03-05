import math


# geeksforgeeks.org: Time Limit Exceeded
def sieveV1(n):
    nums = [True for x in range(n+1)]
    nums[0] = False
    nums[1] = False

    p = 2
    while True:
        for i in range(p*2, n+1, p):
            nums[i] = False

        prev = p
        for i in range(n+1):
            if nums[i] and i > p:
                p = i
                break

        if prev == p:
            break

    primes = []
    for i in range(n+1):
        if nums[i]:
            primes.append(i)

    return primes


def sieveV2(n):
    nums = [True for x in range(n+1)]
    nums[0] = False
    nums[1] = False

    p = 2
    while p*p <= n:
        for i in range(p*p, n+1, p):
            nums[i] = False

        for i in range(2, n+1):
            if nums[i] and i > p:
                p = i
                break

    primes = []
    for i in range(2, n+1):
        if nums[i]:
            primes.append(i)

    return primes


def sieveV3(n):
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


# geeksforgeeks.org: Wrong Answer
def segmentedSieveV1(n):
    def sieve(lo, hi, primes):
        nums = [True for x in range(lo, hi+1)]
        if lo == 0:  # simple sieve
            nums[0] = False
            nums[1] = False

            p = 2
            while p*p < hi:
                if nums[p]:
                    for i in range(p*p, hi+1, p):
                        nums[i] = False
                p += 1
        else:
            for p in primes:
                for i in range(p*p, hi+1, p):
                    if i-lo >= 0:
                        nums[i-lo] = False

        for i in range(lo, hi+1):
            if nums[i-lo]:
                primes.append(i)

    limit = int(math.sqrt(n) + 1)
    lo = 0
    hi = lo + limit
    primes = []
    while lo < n:
        hi = min(hi, n)
        sieve(lo, hi, primes)
        lo += limit+1
        hi = lo + limit

    return primes


# geeksforgeeks.org: Time Limit Exceeded
def segmentedSieveV2(n):
    def simpleSieve(n):
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

    def segSieve(lo, hi, primes):
        nums = [True for x in range(lo, hi+1)]

        for p in primes:
            if p*p > hi:
                break
            for i in range(p*p, hi+1, p):
                if i-lo >= 0:
                    nums[i-lo] = False

        for i in range(lo, hi+1):
            if nums[i-lo]:
                primes.append(i)

    limit = int(math.sqrt(n) + 1)
    primes = simpleSieve(limit)
    lo = limit+1
    hi = lo + limit
    while lo < n:
        hi = min(hi, n)
        segSieve(lo, hi, primes)
        lo += limit+1
        hi = lo + limit

    return primes


class Solution:
    def sieveOfEratosthenes(self, N):
        # return sieveV1(N)
        # return sieveV2(N)
        return sieveV3(N)
        # return segmentedSieveV1(N)
        # return segmentedSieveV2(N)


# ------------------------------------------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        print(*ans)
