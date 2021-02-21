def binarySearch(arr, l, r, value):
    while l <= r:
        index = (l+r) // 2
        middle = arr[index]

        if middle == value:
            return index
        elif middle < value:
            l = index + 1
        else:
            r = index - 1

    return -1


def searchInRotatedArray(arr, value):
    def binaryFindRotatedPoint(arr, l, r):
        while l <= r:
            m = (l+r) // 2
            v = arr[m]

            if m < r and arr[m+1] < v:
                return m+1
            elif l < m and v < arr[m-1]:
                return m
            elif arr[r] < v:
                l = m + 1
            else:
                r = m - 1

        return -1

    l = 0
    r = len(arr) - 1

    rp = binaryFindRotatedPoint(arr, 0, r)
    if rp == -1:
        return binarySearch(arr, l, r, value)

    assert arr[rp] < arr[rp-1]
    if rp+1 < len(arr):
        assert arr[rp] <= arr[rp+1], (rp, arr)

    i = binarySearch(arr, l, rp-1, value)
    if i != -1:
        return i
    return binarySearch(arr, rp, r, value)


def searchInRotatedArrayV2(arr, value):
    def findRotatedPoint(arr):
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                return i
        return -1

    l = 0
    r = len(arr) - 1

    rp = findRotatedPoint(arr)
    if rp == -1:
        return binarySearch(arr, l, r, value)

    i = binarySearch(arr, l, rp-1, value)
    if i != -1:
        return i
    return binarySearch(arr, rp, r, value)


def searchInRotatedArrayV1(arr, value):
    def splitByRotatedPoint(arr):
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                return [arr[0:i], arr[i:]]

        return [arr]

    arrs = splitByRotatedPoint(arr)
    index = 0
    for a in arrs:
        i = binarySearch(a, 0, len(a)-1, value)
        if i != -1:
            return i+index
        index += len(a)

    return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        input()
        n = input()
        arr = [int(x.strip()) for x in input().strip().split(" ")]
        value = int(input().strip())
        r = searchInRotatedArray(arr, value)
        print(r)
