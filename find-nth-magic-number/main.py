def nthFaithfulNumV1(N):
    def intToBitArray(num):
        bits = [int(bit) for bit in "{0:b}".format(num)]
        bits.reverse()
        return bits

    return sum(bit * pow(7, i)
               for i, bit in enumerate(intToBitArray(N)))


def nthFaithfulNumV2(N):
    def intToBitArray(num):
        bits = []
        while num > 0:
            bits.append(num % 2)
            num = num // 2
        return bits

    res = 0
    for i, bit in enumerate(intToBitArray(N)):
        res += bit * pow(7, i)

    return res


class Solution:
    def nthFaithfulNum(self, N):
        # return nthFaithfulNumV1(N)
        return nthFaithfulNumV2(N)

# ---------------------------


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        ob = Solution()
        print(ob.nthFaithfulNum(N))
