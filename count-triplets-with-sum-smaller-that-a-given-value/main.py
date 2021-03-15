# Time Limit Exceeded
def countTripletsV1(arr, n, sum):
    count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k]) < sum:
                    count += 1

    return count


# Time Limit Exceeded
def countTripletsV2(arr, n, sum):
    arr.sort()

    count = 0
    for i in range(0, n):
        if (arr[i]) >= sum:
            break

        for j in range(i+1, n):
            if (arr[i] + arr[j]) >= sum:
                break

            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k]) >= sum:
                    break

                count += 1

    return count


# Time Limit Exceeded
def countTripletsV3(arr, n, sum):
    arr.sort()
    count = 0
    for k in range(n-2):
        l = k + 1
        r = n - 1
        while l < r:
            if arr[l] + arr[k] + arr[r] < sum:
                count += r - l
                l += 1
            else:
                r -= 1

    return count


class Solution:
    def countTriplets(self, arr, n, sum):
        # return countTripletsV1(arr, n, sum)
        # return countTripletsV2(arr, n, sum)
        return countTripletsV3(arr, n, sum)


# ---------------------
if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        input()
        l = list(map(int, input().split()))
        n = l[0]
        k = l[1]
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.countTriplets(a, n, k)
        print(ans)
