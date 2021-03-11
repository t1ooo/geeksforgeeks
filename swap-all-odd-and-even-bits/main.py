# Expected Time Limit
def swapBitsV1(num):
    # def getBit(num, i):
    # return (num & ( 1 << i )) >> i

    def getBit(num, i):
        return (num >> i) & 1

    def setBit(num, i):
        return num | (1 << i)

    def resetBit(num, i):
        return num & ~(1 << i)

    def swap(num, i, k):
        ib = getBit(num, i)
        kb = getBit(num, k)

        if ib == kb:
            return num

        if ib == 1:
            i, k = k, i

        num = setBit(num, i)
        num = resetBit(num, k)
        return num

    for i in range(1, 32, 2):
        num = swap(num, i, i-1)

    return num


# Time Limit Exceeded
def swapBitsV2(num):
    def getBit(num, i):
        return (num >> i) & 1

    def swap(num, i, k):
        ib = getBit(num, i)
        kb = getBit(num, k)

        if ib == kb:
            return num

        x = ib ^ kb
        x = (x << i) | (x << k)

        return num ^ x

    for i in range(1, 32, 2):
        num = swap(num, i, i-1)

    return num


def swapBitsV3(x):
    # Get all even bits of x
    evnBits = x & 0b10101010101010101010101010101010

    # Get all odd bits of x
    oddBits = x & 0b01010101010101010101010101010101

    # Right shift even bits
    evnBits = evnBits >> 1

    # Left shift odd bits
    oddBits = oddBits << 1

    # Combine even and odd bits
    return evnBits | oddBits


class Solution:
    def swapBits(self, n):
        # return swapBitsV1(n)
        # return swapBitsV2(n)
        return swapBitsV3(n)


# -----------------------------
if __name__ == "__main__":
    T = int(input())
    while(T > 0):
        input()
        n = int(input())
        ob = Solution()
        print(ob.swapBits(n))
        T -= 1
