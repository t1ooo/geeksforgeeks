def zigZagV1(arr, n):
    for i in range(n-1):
        k = i + 1
        if (i % 2 == 0 and arr[i] > arr[k]) or (i % 2 == 1 and arr[i] < arr[k]):
            arr[i], arr[k] = arr[k], arr[i]


class Solution:
    def zigZag(self, arr, n):
        return zigZagV1(arr, n)


# ------------------
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        input()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.zigZag(arr, n)
        print(*arr)
        tc -= 1
