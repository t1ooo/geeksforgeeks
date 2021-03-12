def searchV1(arr, n):
    from collections import Counter

    d = Counter(arr)
    for v, count in d.items():
        if count == 1:
            return v

    return None


def searchV2(arr, n):
    if n == 1:
        return arr[0]

    # check first
    if arr[0] != arr[1]:
        return arr[0]

    # check last
    if arr[n-2] != arr[n-1]:
        return arr[n-1]

    # check middle
    for i in range(2+1, n-1):
        a, b, c = arr[i-2], arr[i-1], arr[i]
        if a != b and b != c:
            return b

    return None


def searchV3(arr, n):
    for i in range(0, n-1, 2):
        if arr[i] != arr[i+1]:
            return arr[i]

    return arr[n-1]


# binary search
def searchV4(arr, n):
    def f(arr, l, r):
        if l == r:
            return arr[l]

        m = (l + r) // 2

        if m % 2 == 0:
            if arr[m] == arr[m + 1]:
                return f(arr, m + 2, r)
            else:
                return f(arr, l, m)
        else:
            if arr[m] == arr[m - 1]:
                return f(arr, m + 1, r)
            else:
                return f(arr, l, m - 1)

    return f(arr, 0, n-1)


def searchV5(arr, n):
    xor = 0
    for v in arr:
        xor = xor ^ v

    return xor


def searchV6(arr, n):
    return 2 * sum(set(arr)) - sum(arr)


# another binary search
def searchV7(arr, n):
    l = 0
    r = n-1
    while l < r:
        m = (l + r) // 2
        even = (m % 2 == 0)
        odd = not even
        if (even and arr[m] == arr[m+1]) or (odd and arr[m-1] == arr[m]):
            l = m+1
        else:
            r = m

    return arr[l]


def searchV8(arr, n):
    INT_SIZE = 32
    res = 0

    # Iterate through every bit
    for i in range(0, INT_SIZE):
        bitsSum = 0
        for v in arr:
            if v & (1 << i):
                bitsSum += 1

        if (bitsSum % 2) != 0:
            res = res | (1 << i)

    return res


class Solution:
    def search(self, A, N):
        # return searchV1(A, N)
        # return searchV2(A, N)
        # return searchV3(A, N)
        # return searchV4(A, N)
        # return searchV5(A, N)
        # return searchV6(A, N)
        # return searchV7(A, N)
        return searchV8(A, N)


# ---------------------
if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        input()
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.search(arr, n))
