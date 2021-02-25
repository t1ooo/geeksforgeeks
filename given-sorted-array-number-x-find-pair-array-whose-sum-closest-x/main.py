def findPairWithClosestSum(arr, x):
    l = 0
    r = len(arr) - 1

    res_l = l
    res_r = r

    min_diff = float("inf")

    while l < r:
        diff = arr[l]+arr[r] - x

        if abs(diff) < min_diff:
            min_diff = abs(diff)
            res_l = l
            res_r = r

        if diff == 0:
            break
        elif diff < 0:  # arr[l]+arr[r] < x
            l += 1
        else:
            r -= 1

    return [arr[res_l], arr[res_r]]


if __name__ == "__main__":
    t = int(input())
    for tcs in range(t):
        input()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x = int(input())
        print(*findPairWithClosestSum(arr, x))
