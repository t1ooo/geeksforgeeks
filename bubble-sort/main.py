def bubbleSort(arr, n):
    def swap(arr, r):
        res = False
        for k in range(1, r):
            if arr[k-1] > arr[k]:
                arr[k-1], arr[k] = arr[k], arr[k-1]
                res = True
        return res

    for i in range(n):
        if not swap(arr, n-i):
            break


def bubbleSortV2(arr, n):
    for i in range(n):
        swap = False
        # Last elements are already in place
        for k in range(1, n-i):
            if arr[k-1] > arr[k]:
                arr[k-1], arr[k] = arr[k], arr[k-1]
                swap = True
        if not swap:
            break


def bubbleSortV1(arr, n):
    swap = True
    while swap:
        swap = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swap = True
        # Last elements are already in place
        n -= 1

class Solution:
    def bubbleSort(self, arr, n):
        bubbleSort(arr, n)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        input()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = arr.copy()
        ob.bubbleSort(res, n)
        print(" ".join(map(str, res)))
        for _ in range(1000):
            res = arr.copy()
            ob.bubbleSort(res, n)
