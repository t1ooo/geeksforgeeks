import math


def modInverseV1(a, m):
    for i in range(1, m):
        if i*a % m == 1:
            return i
    return -1


def modInverseV2(a, m):
    tmp = a
    for i in range(1, m):
        if tmp % m == 1:
            return i
        tmp += a
    return -1


class Solution:
    def modInverse(self, a, m):
        # return modInverseV1(a, m)
        return modInverseV2(a, m)

# --------------------


def main():
    T = int(input())
    while(T > 0):
        input()
        am = [int(x) for x in input().strip().split()]
        a = am[0]
        m = am[1]
        ob = Solution()
        print(ob.modInverse(a, m))
        T -= 1


if __name__ == "__main__":
    main()
