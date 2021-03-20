# Time Limit Exceeded
def findSmallestV1(arr, n):
    s = set([0])
    for a in arr:
        s.update([v+a for v in s])

    i = 1
    while i in s:
        i += 1

    return i


def findSmallestV2(arr, n):
    res = 1
    for v in arr:
        if v <= res:
            res += v
        else:
            break

    return res


class Solution:
    def findSmallest(self, arr, n):
        # return findSmallestV1(arr, n)
        return findSmallestV2(arr, n)


# ---------------------------
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        input()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSmallest(arr, n)
        print(ans)
        tc -= 1
