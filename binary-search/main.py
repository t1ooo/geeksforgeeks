def binarySearchRec(arr, l, r, value):
    if r < l:
        return -1

    index = (l+r) // 2
    middle = arr[index]

    if middle == value:
        return index
    elif middle < value:
        l = index + 1
        return binarySearchRec(arr, l, r, value)
    else:
        r = index - 1
        return binarySearchRec(arr, l, r, value)


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


def searchInSorted(arr, N, value):
    i = binarySearch(arr, 0, N-1, value)
    if i == -1:
        return -1
    else:
        return 1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        A = [int(x) for x in input().strip().split()]
        print(searchInSorted(A, N, K))
