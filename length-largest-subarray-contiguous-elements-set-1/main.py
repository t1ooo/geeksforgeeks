def largestSubarrayLengthV1(arr):
    def isContinuousSequence(arr):
        for i in range(1, len(arr)):
            if arr[i-1] + 1 != arr[i]:
                return False
        return True

    if len(arr) == 0:
        return 0

    ln = len(arr)
    while ln > 1:
        for i in range(len(arr)-ln+1):
            tmp = arr[i:i+ln]
            # print(tmp)
            tmp.sort()
            if isContinuousSequence(tmp):
                return ln
        ln -= 1

    return 1


def largestSubarrayLengthV2(arr):
    def isContinuousSequence(arr):
        return len(arr) == max(arr)-min(arr)+1

    if len(arr) == 0:
        return 0

    ln = len(arr)
    while ln > 1:
        for i in range(len(arr)-ln+1):
            tmp = arr[i:i+ln]
            # print(tmp)
            if isContinuousSequence(tmp):
                return ln
        ln -= 1

    return 1


def largestSubarrayLengthV3(arr):
    n = len(arr)

    max_len = 1
    for i in range(n):
        mini = arr[i]
        maxi = arr[i]

        for k in range(i + 1, n):
            mini = min(mini, arr[k])
            maxi = max(maxi, arr[k])

            if maxi - mini == k - i:
                max_len = max(max_len, maxi - mini + 1)

    return max_len


# -----------------------------
arr = [10, 12, 11]
r = 3

x = largestSubarrayLengthV1(arr)
assert r == x, (r, x)

x = largestSubarrayLengthV2(arr)
assert r == x, (r, x)

x = largestSubarrayLengthV3(arr)
assert r == x, (r, x)

# -----------------------------
arr = [14, 12, 11, 20]
r = 2

x = largestSubarrayLengthV1(arr)
assert r == x, (r, x)

x = largestSubarrayLengthV2(arr)
assert r == x, (r, x)

x = largestSubarrayLengthV3(arr)
assert r == x, (r, x)

# -----------------------------
arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
r = 5

x = largestSubarrayLengthV1(arr)
assert r == x, (r, x)

x = largestSubarrayLengthV2(arr)
assert r == x, (r, x)

x = largestSubarrayLengthV3(arr)
assert r == x, (r, x)


# -----------------------------
arr = [1, 3, 45, 4]
r = 1

x = largestSubarrayLengthV1(arr)
assert r == x, (r, x)

x = largestSubarrayLengthV2(arr)
assert r == x, (r, x)

x = largestSubarrayLengthV3(arr)
assert r == x, (r, x)


# -----------------------------
arr = [13, 0, 11, 12]
r = 2

x = largestSubarrayLengthV1(arr)
assert r == x, (r, x)

x = largestSubarrayLengthV2(arr)
assert r == x, (r, x)

x = largestSubarrayLengthV3(arr)
assert r == x, (r, x)
