def largestPrimeFactor(n):
    def primeFactors(n):
        primes = []
        while n % 2 == 0:
            primes.append(2)
            n //= 2

        for i in range(3, int(pow(n, 0.5))+1, 2):
            while n % i == 0:
                primes.append(i)
                n //= i

        if n > 2:
            primes.append(n)

        return primes

    return max(primeFactors(n))


class Solution:
    def largestPrimeFactor(self, N):
        return largestPrimeFactor(N)


# -----------------------------
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        ob = Solution()
        print(ob.largestPrimeFactor(N))
