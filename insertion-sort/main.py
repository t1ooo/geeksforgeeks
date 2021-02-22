import bisect as bsct


def binaryInsertionSort(arr, n):
    def bisect_left(arr, l, r, val):
        r -= 1
        while l <= r:
            m = (l + r)//2
            v = arr[m]
            if v < val:
                l = m + 1
            else:
                r = m - 1
        return r+1

    def move(arr, l, r):
        while l < r:
            arr[r] = arr[r-1]
            r -= 1

    for i in range(1, n):
        curr = arr[i]
        k = bisect_left(arr, 0, i, curr)
        assert k == bsct.bisect_left(arr, curr, lo=0, hi=i)
        if k != i:
            move(arr, k, i)
            arr[k] = curr


def insertionSortV2(arr, n):
    for i in range(1, n):
        curr = arr[i]
        while i >= 1 and curr < arr[i-1]:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = curr


def insertionSortV1(arr, n):
    for i in range(1, n):
        curr = arr[i]
        k = i - 1
        while k >= 0 and curr < arr[k]:
            arr[k+1] = arr[k]
            k -= 1
        arr[k+1] = curr


class Solution:
    def insertionSort(self, arr, n):
        binaryInsertionSort(arr, n)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        input()
        n = int(input())

        arr = list(map(int, input().split()))
        res = arr.copy()
        Solution().insertionSort(res, n)
        print(" ".join(map(str, res)))
        for _ in range(1000):
            res = arr.copy()
            Solution().insertionSort(res, n)
