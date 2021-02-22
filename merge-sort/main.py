import bisect


# in-place sort
def mergeSortV2(arr, l, r):
    def move(arr, l, r):
        while l < r:
            arr[r] = arr[r-1]
            r -= 1

    # use modified binary insertion sort
    def merge(arr, l, m, r):
        for i in range(m+1, r+1):
            curr = arr[i]
            k = bisect.bisect_left(arr, curr, lo=l, hi=i)
            if k == i:
                return
            else:
                move(arr, k, i)
                arr[k] = curr

    def sort(arr, l, r):
        if r <= l:
            return

        m = (l + r) // 2
        sort(arr, l, m)
        sort(arr, m+1, r)
        merge(arr, l, m, r)

    sort(arr, l, r)


def mergeSortV1(arr, l, r):
    def merge(lchunk, rchunk):
        res = []
        li = 0
        ri = 0
        while li < len(lchunk) and ri < len(rchunk):
            lv = lchunk[li]
            rv = rchunk[ri]
            if lv < rv:
                res.append(lv)
                li += 1
            else:
                res.append(rv)
                ri += 1

        res += lchunk[li:]
        res += rchunk[ri:]
        return res

    def sort(arr):
        if len(arr) <= 1:
            return arr

        m = (len(arr) - 1) // 2
        lchunk = sort(arr[:m+1])
        rchunk = sort(arr[m+1:])
        return merge(lchunk, rchunk)

    res = sort(arr)
    for i in range(len(res)):
        arr[i] = res[i]


class Solution:
    def mergeSort(self, arr, l, r):
        mergeSortV2(arr, l, r)
        # mergeSortV1(arr, l, r)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        input()
        n = int(input())
        arr = list(map(int, input().split()))
        res = arr.copy()
        Solution().mergeSort(res, 0, n-1)
        print(" ".join(map(str, res)))
        for _ in range(10000):
            Solution().mergeSort(res, 0, n-1)
