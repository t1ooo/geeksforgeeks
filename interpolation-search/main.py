def interpolationSearch(arr, lo, hi, value):
    if hi < lo or value < arr[lo] or value > arr[hi]:
        return -1

    i = lo + ((value-arr[lo])*(hi-lo) // (arr[hi]-arr[lo]))
    if arr[i] == value:
        return i
    elif arr[i] < value:
        lo = i + 1
        return interpolationSearch(arr, lo, hi, value)
    else:
        hi = i - 1
        return interpolationSearch(arr, lo, hi, value)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        A = [int(x) for x in input().strip().split()]
        print(interpolationSearch(A, 0, N-1, K))
