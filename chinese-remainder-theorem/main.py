# x % num[i] == rem[i]
def findMinXv1(num, rem, k):
    def check(x, num, rem, k):
        for i in range(k):
            if x % num[i] != rem[i]:
                return False
        return True

    x = 0
    while True:
        if check(x, num, rem, k):
            break
        x += 1

    return x


# x = (rem[0]*pp[0]*inv[0] + rem[1]*pp[1]*inv[1] + ...) % prod
#
# prod is product of all given numbers
# prod = num[0] * num[1] * ... * num[k-1]
#
# pp[i] is product of all divided by num[i]
# pp[i] = prod / num[i]
#
# inv[i] = Modular Multiplicative Inverse of pp[i] with respect to num[i]
def findMinXv2(num, rem, k):
    def product(arr):
        res = 1
        for v in arr:
            res *= v
        return res

    def modInverse(a, m):
        for i in range(1, m):
            if i*a % m == 1:
                return i
        return -1

    prod = product(num)
    pp = [prod / num[i] for i in range(k)]
    inv = [modInverse(pp[i], num[i]) for i in range(k)]
    return sum([rem[i]*pp[i]*inv[i] for i in range(k)]) % prod


num = [3, 4, 5]
rem = [2, 3, 1]
k = len(num)
assert findMinXv1(num, rem, k) == 11
assert findMinXv2(num, rem, k) == 11

num = [2, 3, 7]
rem = [1, 2, 6]
k = len(num)
assert findMinXv1(num, rem, k) == 41
assert findMinXv2(num, rem, k) == 41
