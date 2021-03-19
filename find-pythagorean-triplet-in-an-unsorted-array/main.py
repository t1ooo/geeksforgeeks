# Time Limit Exceeded
def checkTripletV1(arr, n):
    arr.sort()
    for a in range(0, n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                if arr[a]**2 + arr[b]**2 == arr[c]**2:
                    return True

    return False


def checkTripletV2(arr, n):
    def binarySearchPow2(arr, l, r, val):
        if r < l:
            return False

        m = (l+r)//2
        v = arr[m]

        if v == val:
            return True
        elif v < val:
            l = m+1
            return binarySearchPow2(arr, l, r, val)
        else:
            r = m-1
            return binarySearchPow2(arr, l, r, val)

    arr.sort()
    for i in range(0, n):
        for k in range(i+1, n):
            c = (arr[i]**2 + arr[k]**2) ** 0.5
            if c == int(c) and binarySearchPow2(arr, k+1, n-1, int(c)):
                return True

    return False


def checkTripletV3(arr, n):
    arr.sort(reverse=True)
    squares = [v**2 for v in arr]

    for k in range(n-2):
        c2 = squares[k]
        l = k+1
        r = n-1
        while l < r:
            a2b2 = squares[l] + squares[r]
            if a2b2 == c2:
                return True
            elif a2b2 < c2:
                r -= 1
            else:
                l += 1

    return False


def checkTripletV4(arr, n):
    def has(hash, key):
        return key < len(hash) and hash[key]

    maximum = max(arr)
    hash = [False] * (maximum+1)

    for v in arr:
        hash[v] = True

    for a in range(1, len(hash)):
        if not has(hash, a):
            continue

        for b in range(a+1, len(hash)):
            if not has(hash, b):
                continue

            c = (a*a + b*b) ** 0.5
            if c == int(c) and has(hash, int(c)):
                return True

    return False


def checkTripletV5(arr, n):
    s = set(arr)
    for i, a in enumerate(s):
        for k, b in enumerate(s):
            if k <= i:
                continue

            c = (a*a + b*b) ** 0.5
            if c == int(c) and int(c) in s:
                return True

    return False


class Solution:
    def checkTriplet(self, arr, n):
        # return checkTripletV1(arr, n)
        # return checkTripletV2(arr, n)
        # return checkTripletV3(arr, n)
        # return checkTripletV4(arr, n)
        return checkTripletV5(arr, n)


# ------------------------------
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        input()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1
