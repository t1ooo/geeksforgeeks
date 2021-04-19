import bisect


# Time Limit Exceeded
def inversionCountV1(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1

    return count


# use insertion sort (Time Limit Exceeded)
def inversionCountV2(arr, n):
    arrSorted = []
    count = 0
    for v in arr:
        k = bisect.bisect_right(arrSorted, v)
        count += len(arrSorted) - k
        arrSorted.insert(k, v)

    return count


# use insertion sort in-place (Time Limit Exceeded)
def inversionCountV3(arr, n):
    def move(arr, l, r):
        while l < r:
            arr[r] = arr[r-1]
            r -= 1

    count = 0
    for i in range(1, n):
        v = arr[i]
        k = bisect.bisect_right(arr, v, lo=0, hi=i)
        if k != i:
            count += i - k
            move(arr, k, i)
            arr[k] = v

    return count


# use merge sort
def inversionCountV4(arr, n):
    def merge(lchunk, rchunk, count):
        res = []
        li = 0
        ri = 0
        while li < len(lchunk) and ri < len(rchunk):
            lv = lchunk[li]
            rv = rchunk[ri]
            if lv <= rv:
                res.append(lv)
                li += 1
            else:
                count[0] += len(lchunk) - li
                res.append(rv)
                ri += 1

        res += lchunk[li:]
        res += rchunk[ri:]
        return res

    def sort(arr, count):
        if len(arr) <= 1:
            return arr

        m = (len(arr) - 1) // 2
        lchunk = sort(arr[:m+1], count)
        rchunk = sort(arr[m+1:], count)
        return merge(lchunk, rchunk, count)

    count = [0]
    sort(arr, count)
    return count[0]


class Solution:
    def inversionCount(self, arr, n):
        # return inversionCountV1(arr, n)
        # return inversionCountV2(arr, n)
        # return inversionCountV3(arr, n)
        return inversionCountV4(arr, n)


# ---------------------
if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        input()
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a, n))
