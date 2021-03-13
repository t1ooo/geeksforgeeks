def countBitsFlipV1(a, b):
    count = 0
    for i in range(32):
        bit1 = (a >> i) & 1
        bit2 = (b >> i) & 1
        if bit1 != bit2:
            count += 1

    return count


def countBitsFlipV2(a, b):
    xor = a ^ b
    bits = format(xor, "b")
    return bits.count("1")


def countBitsFlipV3(a, b):
    def countSetBits(n):
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
        return count

    xor = a ^ b
    return countSetBits(xor)


def countBitsFlipV4(a, b):
    def countSetBits(n):
        count = 0
        while n > 0:
            count += 1
            n &= n - 1
        return count

    xor = a ^ b
    return countSetBits(xor)


class Solution:
    def countBitsFlip(self, a, b):
        # return countBitsFlipV1(a, b)
        # return countBitsFlipV2(a, b)
        # return countBitsFlipV3(a, b)
        return countBitsFlipV4(a, b)


# -----------------------------
if __name__ == "__main__":
    T = int(input())
    while(T > 0):
        input()
        ab = [int(x) for x in input().strip().split()]
        a = ab[0]
        b = ab[1]
        ob = Solution()
        print(ob.countBitsFlip(a, b))
        T -= 1
