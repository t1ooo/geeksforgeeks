MOD = 1000000007


# built-in
def powerV1(base, exp):
    return pow(base, exp, MOD)


# Time Limit Exceeded
def powerV2(base, exp):
    def f(base, exp):
        if exp == 0:
            return 1

        tmp = f(base, exp // 2)
        if exp % 2 == 0:
            return tmp * tmp
        else:
            return base * tmp * tmp

    return f(base, exp) % MOD


def powerV3(base, exp):
    def f(base, exp):
        if exp == 0:
            return 1
        if base == 0:
            return 0
        return base * f(base, exp - 1)

    return f(base, exp) % MOD


def powerV4(base, exp):
    def f(base, exp):    
        res = 1
        while exp > 0:
            if exp % 2 == 1:
                res = res * base
            exp = exp // 2
            base = base * base

    return f(base, exp) % MOD


def powerV5(base, exp):
    def f(base, exp, mod):    
        res = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                res = (res * base) % mod
            exp = exp // 2
            base = (base * base) % mod

    return f(base, exp, MOD)

class Solution:
    def power(self, N, R):
        # return powerV1(N, R)
        # return powerV2(N, R)
        # return powerV3(N, R)
        # return powerV4(N, R)
        return powerV5(N, R)


if __name__ == "__main__":
    T = int(input())
    while(T > 0):
        input()
        N = input()
        R = N[::-1]
        ob = Solution()
        ans = ob.power(int(N), int(R))
        print(ans)
        T -= 1
