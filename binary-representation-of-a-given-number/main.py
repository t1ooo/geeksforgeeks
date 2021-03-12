def getBinaryRepV1(n):
    return bin(n)[2:].rjust(30, "0")


def getBinaryRepV2(n):
    return "{0:b}".format(n).rjust(30, "0")


def getBinaryRepV3(n):
    return format(n, "b").rjust(30, "0")


def getBinaryRepV4(n):
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n = n // 2

    return "".join(reversed(bits)).rjust(30, "0")


def getBinaryRepV5(n):
    res = []
    for i in range(30):
        bit = (n >> i) & 1
        res.append(str(bit))

    return "".join(reversed(res))


class Solution:
    def getBinaryRep(self, n):
        # return getBinaryRepV1(n)
        # return getBinaryRepV2(n)
        # return getBinaryRepV3(n)
        # return getBinaryRepV4(n)
        return getBinaryRepV5(n)


# -----------------------------
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        input()
        n = int(input())
        ob = Solution()
        ans = ob.getBinaryRep(n)
        print(ans)
