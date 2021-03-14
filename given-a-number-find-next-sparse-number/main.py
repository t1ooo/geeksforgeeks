def nextSparseV1(n):
    def isSparse(n):
        bits = format(n, "b")
        for i in range(1, len(bits)):
            if bits[i-1] == "1" and bits[i] == "1":
                return False
        return True

    while True:
        if isSparse(n):
            return n
        n += 1


def nextSparseV2(n):
    while "11" in format(n, "b"):
        n += 1

    return n


def nextSparseV3(n):
    def isSparse(n):
        if n & (n << 1) == 0:
            return True
        return False

    while not isSparse(n):
        n += 1

    return n


def nextSparseV4(n):
    for i in range(32):
        if (n & (0b11 << i)) == (0b11 << i):
            n += 1 << i
            n &= ((~0) >> i) << (i + 2)
    return n


def nextSparseV5(x):
    bits = list(format(x, "b"))
    bits.reverse()
    bits.append("0")

    n = len(bits)
    last_final = 0
    for i in range(1, n - 1):
        if bits[i-1] == "1" and bits[i] == "1" and bits[i+1] == "0":
            bits[i+1] = "1"

            for k in range(last_final, i+1):
                bits[k] = "0"

            last_final = i + 1

    return int("".join(reversed(bits)), 2)


def nextSparseV6(x):
    bits = ["0"] + list(format(x, "b"))

    last_final = len(bits)
    i = len(bits) - 2
    while i > 0:
        if bits[i-1:i+2] == ["0", "1", "1"]:
            bits[i-1] = "1"

            for k in range(i, last_final):
                bits[k] = "0"

            last_final = i

        i -= 1

    return int("".join(bits), 2)


class Solution:
    def nextSparse(ob, n):
        # return nextSparseV1(n)
        # return nextSparseV2(n)
        # return nextSparseV3(n)
        # return nextSparseV4(n)
        # return nextSparseV5(n)
        return nextSparseV6(n)


# ---------------------------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        n = int(input())
        ob = Solution()
        print(ob.nextSparse(n))
