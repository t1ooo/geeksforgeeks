# Time Limit Exceeded
def countSetBitsV1(n):
    return sum(format(i, "b").count("1") for i in range(1, n+1))


# Time Limit Exceeded
BITS = [0]


def countSetBitsV2(n):
    global BITS
    if len(BITS) < n:
        for i in range(len(BITS), n+1):
            BITS.append(BITS[i-1] + format(i, "b").count("1"))

    return BITS[n]


def countSetBitsV3(N):
    two = 2
    ans = 0
    n = N
    while n != 0:
        ans += (N // two) * (two >> 1)
        if (N & (two - 1)) > (two >> 1) - 1:
            ans += (N & (two - 1)) - (two >> 1) + 1
        two <<= 1
        n >>= 1

    return ans


def countSetBitsV4(n):
    n += 1
    count = 0

    for i in range(1, n):
        x = pow(2, i)
        x2 = x // 2
        if not (x2 < n):
            break

        count += (n // x) * (x2)
        if (n % x) > x2:
            count += (n % x) - x2

    return count


def countSetBitsV5(n):
    n += 1
    x = 2
    count = n // 2
    while x <= n:
        totalPairs = n // x
        count += (totalPairs // 2) * x
        if totalPairs % 2 == 1:
            count += n % x
        x = x * 2

    return count


class Solution:
    def countSetBits(self, n):
        # return countSetBitsV1(n)
        # return countSetBitsV2(n)
        # return countSetBitsV3(n)
        # return countSetBitsV4(n)
        return countSetBitsV5(n)


# ----------------
if __name__ == "__main__":
    for _ in range(int(input())):
        input()
        ob = Solution()
        print(ob.countSetBits(int(input())))
