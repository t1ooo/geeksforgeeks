INT_LEN = 32
MOD = pow(10, 9)+7


# Time Limit Exceeded
def countBitsV1(N, A):
    def intToBitArray(num):
        n = 1 if num < 0 else 0
        num = abs(num)
        len = INT_LEN - 1
        bits = [n] + [int(bit) for bit in "{0:b}".format(num).rjust(len, "0")]
        bits.reverse()
        return bits

    def bitDiff(bits1, bits2):
        diff = 0
        for i in range(len(bits1)):
            if bits1[i] != bits2[i]:
                diff += 1
        return diff

    A = set(A)
    N = len(A)
    res = 0
    bits = [intToBitArray(num) for num in A]
    for i in range(0, N):
        for k in range(i+1, N):
            res += bitDiff(bits[i], bits[k]) * 2

    return res % MOD


# Time Limit Exceeded
def countBitsV2(N, A):
    def intToBitArray(num):
        signBit = 1 if num < 0 else 0
        num = abs(num)
        bits = []
        while num > 0:
            bits.append(num % 2)
            num = num // 2
        ln = INT_LEN-1-len(bits)
        bits += [0]*ln
        bits.append(signBit)
        return bits

    def bitDiff(bits1, bits2):
        diff = 0
        for i in range(len(bits1)):
            if bits1[i] != bits2[i]:
                diff += 1
        return diff

    A = set(A)
    N = len(A)
    res = 0
    bits = [intToBitArray(num) for num in A]
    for i in range(0, N):
        for k in range(i+1, N):
            res += bitDiff(bits[i], bits[k]) * 2

    return res % MOD


def countBitsV3(N, A):
    # Two's complement
    def intToBitArray(num):
        if num < 0:
            num = (1 << INT_LEN) + num
        padLen = INT_LEN
        bits = [int(bit) for bit in "{0:b}".format(num).rjust(padLen, "0")]
        bits.reverse()
        return bits

    res = 0
    bits = [intToBitArray(num) for num in A]
    for i in range(INT_LEN):
        count = sum(bit[i] for bit in bits)
        res += (count * (N - count) * 2)

    return res % MOD


def countBitsV4(N, A):
    def intToBitArray(num):
        bits = []
        for i in range(0, INT_LEN):
            if num & (1 << i):
                bits.append(1)
            else:
                bits.append(0)
        return bits

    res = 0
    bits = [intToBitArray(num) for num in A]
    for i in range(INT_LEN):
        count = sum(bit[i] for bit in bits)
        res += (count * (N - count) * 2)

    return res % MOD


def countBitsV5(n, arr):
    res = 0
    for i in range(INT_LEN):
        count = 0
        for num in arr:
            if num & (1 << i): # check i-th bit
                count += 1
        res += (count * (n - count)) * 2

    return res % MOD


class Solution:
    def countBits(self, N, A):
        try:
            # return countBitsV1(N, A)
            # return countBitsV2(N, A)
            # return countBitsV3(N, A)
            # return countBitsV4(N, A)
            return countBitsV5(N, A)
        except Exception as e:
            print(e)


# ----------------------------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        A = input().split()
        for it in range(N):
            A[it] = int(A[it])
        ob = Solution()
        print(ob.countBits(N, A))
