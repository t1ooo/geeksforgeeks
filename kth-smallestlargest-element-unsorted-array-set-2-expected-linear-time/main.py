import bisect
import random


def swap(arr, i, k):
    arr[i], arr[k] = arr[k], arr[i]


# use median of medians
def kthSmallestV8(arr, l, r, k):
    def median(arr):
        arr.sort()
        return arr[len(arr)//2]

    def medianOfMedian(arr):
        medians = []
        n = 5
        for i in range(0, len(arr), n):
            medians.append(median(arr[i:i+n]))

        if len(medians) == 1:
            return medians[0]
        else:
            return medianOfMedian(medians)

    def lomutoPartition(arr, l, r):
        pivot = arr[r]
        i = l
        for k in range(l, r):
            if arr[k] < pivot:
                swap(arr, i, k)
                i += 1
        swap(arr, i, r)
        return i

    def partition(arr, l, r, m):
        # move m to end
        for i in range(l, r):
            if arr[i] == m:
                swap(arr, r, i)
                break

        return lomutoPartition(arr, l, r)

    def f(arr, l, r, k):
        m = medianOfMedian(arr[l:r+1])
        p = partition(arr, l, r, m)
        i = k - 1
        if p == i:
            return arr[p]

        if i < p:
            return f(arr, l, p-1, k)
        else:
            return f(arr, p+1, r, k)

    return f(arr, l, r, k)


# use min heap
def kthSmallestV7(arr, l, r, k):
    def heapify(arr, size, i):
        smallest = i  # smallest value index

        li = (i*2) + 1  # left child index
        ri = (i*2) + 2  # right child index

        if li < size and arr[li] < arr[smallest]:
            smallest = li
        if ri < size and arr[ri] < arr[smallest]:
            smallest = ri

        if smallest != i:
            swap(arr, i, smallest)
            heapify(arr, size, smallest)

    size = len(arr)

    # build min heap
    i = len(arr)//2 - 1
    while i >= 0:
        heapify(arr, size, i)
        i -= 1

    i = size - 1
    while i > 0:
        swap(arr, 0, i)
        heapify(arr, i, 0)
        if i == size-k:
            return arr[i]
        i -= 1

    return arr[size-k]


# use max heap
def kthSmallestV6(arr, l, r, k):
    def heapify(arr, size, i):
        largest = i  # largest value index

        li = (i*2) + 1  # left child index
        ri = (i*2) + 2  # right child index

        if li < size and arr[largest] < arr[li]:
            largest = li
        if ri < size and arr[largest] < arr[ri]:
            largest = ri

        if largest != i:
            swap(arr, i, largest)
            heapify(arr, size, largest)

    size = len(arr)

    # build max heap
    i = len(arr)//2 - 1
    while i >= 0:
        heapify(arr, size, i)
        i -= 1

    i = size - 1
    while i > 0:
        swap(arr, 0, i)
        heapify(arr, i, 0)
        if i == k-1:
            return arr[i]
        i -= 1

    return arr[k-1]


# use quick select (Hoare partition scheme)
def kthSmallestV5(arr, l, r, k):
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

    def f(arr, l, r, k):
        if l == r:
            return arr[l]

        i = k - 1
        p = partition(arr, l, r)

        if i <= p:
            return f(arr, l, p, k)
        else:
            return f(arr, p+1, r, k)

    return f(arr, l, r, k)


# use quick select wiht random pivot (# Lomuto partition scheme)
def kthSmallestV4(arr, l, r, k):
    def partition(arr, l, r):
        pivot = arr[r]
        i = l
        for k in range(l, r):
            if arr[k] < pivot:
                swap(arr, i, k)
                i += 1
        swap(arr, i, r)
        return i

    def randomPartition(arr, l, r):
        pivot = random.randrange(l, r+1)
        swap(arr, pivot, r)
        return partition(arr, l, r)

    def f(arr, l, r, k):
        if l == r:
            return arr[l]

        i = k - 1
        p = randomPartition(arr, l, r)
        if p == i:
            return arr[p]

        if i < p:
            return f(arr, l, p-1, k)
        else:
            return f(arr, p+1, r, k)

    return f(arr, l, r, k)


# use quick select (# Lomuto partition scheme)
def kthSmallestV3(arr, l, r, k):
    def partition(arr, l, r):
        pivot = arr[r]
        i = l
        for k in range(l, r):
            if arr[k] < pivot:
                swap(arr, i, k)
                i += 1
        swap(arr, i, r)
        return i

    def f(arr, l, r, k):
        if l == r:
            return arr[l]

        i = k - 1
        p = partition(arr, l, r)
        if p == i:
            return arr[p]

        if i < p:
            return f(arr, l, p-1, k)
        else:
            return f(arr, p+1, r, k)

    return f(arr, l, r, k)


# use bubble sort
def kthSmallestV2(arr, l, r, k):
    isswap = True
    left = l + 1
    right = r + 1
    kk = k
    while isswap and kk > 0:
        isswap = False
        for i in range(left, right):
            if arr[i-1] < arr[i]:
                swap(arr, i-1, i)
                isswap = True
        right -= 1
        kk -= 1
    return arr[r+1-k]


# use sorted temp array
def kthSmallestV1(arr, l, r, k):
    def insert(arr, i, v):
        # move other elements to the right
        k = len(arr) - 1
        while k >= i + 1:
            arr[k] = arr[k-1]
            k -= 1
        # insert
        arr[i] = v

    smallests = [float("inf")] * k
    for i in range(l, r+1):
        x = bisect.bisect_left(smallests, arr[i])
        if x == k:
            continue
        insert(smallests, x, arr[i])

    return smallests[k-1]


def kthSmallest(arr, l, r, k):
    return kthSmallestV8(arr, l, r, k)
    # return kthSmallestV7(arr, l, r, k)
    # return kthSmallestV6(arr, l, r, k)
    # return kthSmallestV5(arr, l, r, k)
    # return kthSmallestV4(arr, l, r, k)
    # return kthSmallestV3(arr, l, r, k)
    # return kthSmallestV2(arr, l, r, k)
    # return kthSmallestV1(arr, l, r, k)


if __name__ == "__main__":
    import random
    t = int(input())
    for tcs in range(t):
        input()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(kthSmallest(arr, 0, n-1, k))
