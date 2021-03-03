import random
import math


# probabilistic primality test: Fermat primality test
def isPrimeV1(n):
    # (a^n)%p in O(logy)
    def power(a, n, p):
        res = 1
        a = a % p
        while n > 0:
            if n % 2:
                res = (res * a) % p
                n = n - 1
            else:
                a = (a ** 2) % p
                n = n // 2

        return res % p

    k = 3
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for _ in range(k):
            a = random.randint(2, n - 2)

            # Fermat's little theorem
            if power(a, n - 1, n) != 1:
                return False

    return True


# simple solution (geeksforgeeks.org: Time Limit Exceeded)
def isPrimeV2(N):
    if N <= 1:
        return False

    for i in range(2, N):
        if N % i == 0:
            return False

    return True


def isPrimeV3(N):
    if N <= 1:
        return False

    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False

    return True


def isPrimeV4(N):
    if N <= 1:
        return False
    if N <= 3:
        return True

    if N % 2 == 0 or N % 3 == 0:
        return False

    i = 5
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i = i + 6

    return True


class Solution:
    def isPrime(self, N):
        return int(
            # isPrimeV1(N)
            # isPrimeV2(N)
            # isPrimeV3(N)
            isPrimeV4(N)
        )

# --------------------------------


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        ob = Solution()
        print(ob.isPrime(N))
