def swap(arr, i, k):
    arr[i], arr[k] = arr[k], arr[i]


def heapifyRec(arr, size, i):
    maxI = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < size and arr[maxI] < arr[l]:
        maxI = l

    if r < size and arr[maxI] < arr[r]:
        maxI = r

    if maxI != i:
        swap(arr, maxI, i)
        heapifyRec(arr, size, maxI)


def heapify(arr, size, i):
    while True:
        maxI = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < size and arr[maxI] < arr[l]:
            maxI = l

        if r < size and arr[maxI] < arr[r]:
            maxI = r

        if maxI == i:
            break

        swap(arr, maxI, i)
        i = maxI


def heapSort(arr, size):
    size = len(arr)

    # build max heap
    i = (size//2) - 1  # index of last node with childs
    while i >= 0:
        heapify(arr, size, i)
        i -= 1

    # extract roots from heap
    i = size - 1 # last index
    while i > 0:
        swap(arr, 0, i)
        heapify(arr, i, 0)
        i -= 1


class Solution:
    def HeapSort(self, arr, n):
        heapSort(arr, n)


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        input()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr, n)
        print(*arr)
