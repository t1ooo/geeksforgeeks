# Time Limit Exceeded
def countTripletsV1(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] < a[j] and a[j] < a[k]:
                    count += 1
    return count


def countTripletsV2(a):
    n = len(a)
    count = 0
    for m in range(1, n-1):
        lower = 0
        for l in range(m):
            if a[l] < a[m]:
                lower += 1

        if lower == 0:
            continue

        greater = 0
        for r in range(m+1, n):
            if a[m] < a[r]:
                greater += 1

        count += lower * greater

    return count


# use binary index tree
def countTripletsV3(a):
    import bisect

    def update(bittree, n, i, val):
        while i <= n:
            bittree[i] += val
            i += i & -i

    def query(bittree, i):
        sum = 0
        while i > 0:
            sum += bittree[i]
            i -= i & -i
        return sum

    def convert(arr, n):
        temp = sorted(arr)
        for i in range(n):
            arr[i] = bisect.bisect_left(temp, arr[i]) + 1

    def getCount(arr, n):
        convert(arr, n)

        smaller_right = [0] * (n + 1)
        greater_left = [0] * (n + 1)

        bittree = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            smaller_right[i] = query(bittree, arr[i] - 1)
            update(bittree, n, arr[i], 1)

        bittree = [0] * (n + 1)
        for i in range(n):
            greater_left[i] = i - query(bittree, arr[i])
            update(bittree, n, arr[i], 1)

        ans = 0
        for i in range(n):
            ans += greater_left[i] * smaller_right[i]

        return ans

    a = list(reversed(a))
    return getCount(a, len(a))


# use binary index tree
def countTripletsV4(a):
    import bisect

    def update(bittree, n, i, val):
        while i <= n:
            bittree[i] += val
            i += i & -i

    def query(bittree, i):
        sum = 0
        while i > 0:
            sum += bittree[i]
            i -= i & -i
        return sum

    def convert(arr, n):
        temp = sorted(arr)
        for i in range(n):
            arr[i] = bisect.bisect_left(temp, arr[i]) + 1

    def getCount(arr, n):
        convert(arr, n)

        bittree1 = [0] * (n + 1)
        bittree2 = [0] * (n + 1)

        ans = 0
        for i in range(n):
            smaller = query(bittree1, a[i] - 1)
            update(bittree1, n, arr[i], 1)

            ans += query(bittree2, a[i] - 1)
            update(bittree2, n, arr[i], smaller)

        return ans

    return getCount(a, len(a))


class Solution:
    def countTriplets(self, nums):
        # return countTripletsV1(nums)
        # return countTripletsV2(nums)
        # return countTripletsV3(nums)
        return countTripletsV4(nums)


# ----------------------
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        input()
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.countTriplets(nums)
        print(ans)
