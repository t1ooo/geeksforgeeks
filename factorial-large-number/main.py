def factorialV1(N):
    res = 1
    for n in range(2, N+1):
        res *= n
    return [int(v) for v in str(res)]


def factorialV2(N):
    def mult(digits, n):
        res = []
        carry = 0
        for digit in digits:
            carry = (digit * n) + carry
            res.append(carry % 10)
            carry = carry // 10

        while carry != 0:
            res.append(carry % 10)
            carry = carry // 10

        return res

    digits = [1]
    for n in range(2, N+1):
        digits = mult(digits, n)

    return reversed(digits)


class Solution:
    def factorial(self, N):
        # return factorialV1(N)
        return factorialV2(N)


# --------------------------------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N)
        for i in ans:
            print(i, end="")
        print()
