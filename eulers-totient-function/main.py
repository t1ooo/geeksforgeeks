import math


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


def gcd(x, y):
    if x == 0:
        return y
    return gcd(y % x, x)


def primeFactorization(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            res.append(i)
            n = n // i

    if n > 2:
        res.append(n)

    res.sort()
    return res


# geeksforgeeks.org: Time Limit Exceeded
def maximizeEulerRatioV1(N):
    def eulerTotientV1(n):
        res = 1
        for i in range(2, n):
            if gcd(i, n) == 1:
                res += 1
        return res

    minN = -1
    maxRation = float("-inf")
    for n in range(1, N+1):
        ratio = n/eulerTotientV1(n)
        if maxRation < ratio:
            maxRation = ratio
            minN = n
    return minN


# geeksforgeeks.org: Time Limit Exceeded
def maximizeEulerRatioV2(N):
    # Φ(6) = 6 * (1-1/2) * (1-1/3) = 2
    def eulerTotientV2(n):
        res = n
        for prime in set(primeFactorization(n)):
            res *= 1-(1/prime)
        return res

    minN = -1
    maxRation = float("-inf")
    for n in range(1, N+1):
        ratio = n/eulerTotientV2(n)
        if maxRation < ratio:
            maxRation = ratio
            minN = n
    return minN


# geeksforgeeks.org: correct
def maximizeEulerRatioV3(N):
    primes = sieveV3(50)
    curr = 1
    for p in primes:
        next = curr * p
        if next > N:
            break
        curr = next
    return curr


class Solution:
    def maximizeEulerRatio(self, N):
        # return maximizeEulerRatioV1(N)
        # return maximizeEulerRatioV2(N)
        return maximizeEulerRatioV3(N)

# -----------------------------


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        ob = Solution()
        print(ob.maximizeEulerRatio(N))
