def copyList(to, from_):
    for i in range(len(from_)):
        to[i] = from_[i]


def swap(arr, i, k):
    arr[i], arr[k] = arr[k], arr[i]


# custom partition scheme
def quickSortV5(arr, l, r):
    def partition(arr, l, r):
        last = r
        pivot = arr[last]
        r -= 1
        while True:
            if arr[l] < pivot:
                l += 1
            elif arr[r] > pivot:
                r -= 1
            elif l < r:
                swap(arr, l, r)
                l += 1
                r -= 1
            else:
                swap(arr, l, last)
                return l

    def sort(arr, l, r):
        if l < r:
            p = partition(arr, l, r)
            # for i in range(l,p+1):
            #     for k in range(p+1,r+1):
            #         assert arr[i] <= arr[k]
            sort(arr, l, p-1)
            sort(arr, p+1, r)

    sort(arr, l, r)


# Lomuto partition scheme
def quickSortV4(arr, l, r):
    def partition(arr, l, r):
        pivot = arr[r]
        i = l
        for k in range(l, r):
            if arr[k] < pivot:
                swap(arr, i, k)
                i += 1
        swap(arr, i, r)
        return i

    def sort(arr, l, r):
        if l < r:
            p = partition(arr, l, r)
            # for i in range(l,r+1):
            #     if i < p: assert arr[i] < arr[p]
            #     if i > p: assert arr[i] >= arr[p]
            sort(arr, l, p-1)
            sort(arr, p+1, r)

    sort(arr, l, r)


# Hoare partition scheme
def quickSortV3(arr, l, r):
    def partition(arr, l, r):
        pivot = arr[(l+r)//2]
        while True:
            if arr[l] < pivot:
                l += 1
            elif arr[r] > pivot:
                r -= 1
            elif l < r:
                swap(arr, l, r)
                l += 1
                r -= 1
            else:
                return r

    def sort(arr, l, r):
        if l < r:
            p = partition(arr, l, r)
            # for i in range(l,p+1):
            #     for k in range(p+1,r+1):
            #         assert arr[i] <= arr[k]
            sort(arr, l, p)
            sort(arr, p+1, r)

    sort(arr, l, r)


# slpit to three groups
def quickSortV2(arr, l, r):
    def sort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        eq = [v for v in arr if v == pivot]
        le = [v for v in arr[1:] if v < pivot]
        gr = [v for v in arr[1:] if v > pivot]
        return sort(le) + eq + sort(gr)

    copyList(arr, sort(arr))


# simple
def quickSortV1(arr, l, r):
    def sort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        le = [v for v in arr[1:] if v <= pivot]
        gr = [v for v in arr[1:] if v > pivot]
        return sort(le) + [pivot] + sort(gr)

    copyList(arr, sort(arr))


class Solution:
    def quickSort(self, arr, low, high):
        # quickSortV5(arr, low, high)
        # quickSortV4(arr, low, high)
        quickSortV3(arr, low, high)
        # quickSortV2(arr, low, high)
        # quickSortV1(arr, low, high)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        input()
        n = int(input())
        arr = list(map(int, input().split()))
        res = arr.copy()
        Solution().quickSort(res, 0, n-1)
        print(*res)
