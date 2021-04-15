def countSort(arr):
    n = len(arr)

    maxi = int(max(arr))
    mini = int(min(arr))

    count = [0] * (maxi - mini + 1)
    output = [0] * n

    for i in range(n):
        count[arr[i]-mini] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(n):
        output[count[arr[i]-mini]-1] = arr[i]
        count[arr[i]-mini] -= 1

    for i in range(n):
        arr[i] = output[i]

    return arr


def countSortV2(arr):
    maxi = max(arr)
    mini = min(arr)

    count = [0] * (maxi-mini+1)
    for v in arr:
        count[v-mini] += 1

    res = []
    for i in range(len(count)):
        while count[i] > 0:
            res.append(i+mini)
            count[i] -= 1

    return res


def mapl(fn, ls):
    return list(map(fn, ls))


def LargestEvenV1(S):
    s = countSort(mapl(int, S))

    for i in range(len(s)):
        if int(s[i]) % 2 == 0:
            tmp = s[i]
            while i > 0:
                s[i] = s[i-1]
                i -= 1
            s[0] = tmp
            break

    return "".join(reversed(mapl(str, s)))


def LargestEvenV2(S):
    s = countSortV2(mapl(int, S))

    for i in range(len(s)):
        if int(s[i]) % 2 == 0:
            s = [s[i]] + s[0:i] + s[i+1:]
            break

    return "".join(reversed(mapl(str, s)))


class Solution:
    def LargestEven(self, S):
        return LargestEvenV1(S)
        # return LargestEvenV2(S)


# --------------------------
if __name__ == '__main__':
    arr = [1, 4, 1, 2, 7, 5, 2]
    assert countSort(arr) == sorted(arr)
    assert countSortV2(arr) == sorted(arr)

    t = int(input())
    for _ in range(t):
        input()
        s = input().strip()
        ob = Solution()
        print(ob.LargestEven(s))
