INT_LEN = 16


def rotateV1(N, D):
    D = D % INT_LEN

    bits = format(N, "b").rjust(INT_LEN, "0")

    left = bits[D:] + bits[:D]
    right = bits[INT_LEN-D:] + bits[:INT_LEN-D]

    return int(left, 2), int(right, 2)


def rotateV2(N, D):
    D = D % INT_LEN

    left = (N << D) | (N >> (INT_LEN - D))
    right = (N >> D) | (N << (INT_LEN - D))

    # cut number to INT_LEN
    mask = int("1" * INT_LEN, 2)  # == 0b1111111111111111
    left = left & mask
    right = right & mask

    return [left, right]


class Solution:
    def rotate(self, N, D):
        # return rotateV1(N, D)
        return rotateV2(N, D)


# --------------------------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0], ans[1])
