import bisect


# use Longest common subsequence problem
def longestSubsequence(a, n):
    def lcs(m, n, X, Y):
        mem = [[0]*(n+1) for i in range(m+1)]
        for i in range(m+1):
            for k in range(n+1):
                if i == 0 or k == 0:
                    mem[i][k] = 0
                elif X[i-1] == Y[k-1]:
                    mem[i][k] = 1 + mem[i-1][k-1]
                else:
                    mem[i][k] = max(mem[i-1][k], mem[i][k-1])
        return mem[m][n]

    b = sorted(set(a))  # remove dublicate and sort
    return lcs(len(a), len(b), a, b)


# O(n log n) with bisect (std::lower_bound in C++)
def longestSubsequenceV4(a, n):
    tail = []
    for v in a:
        index = bisect.bisect_left(tail, v)
        if index == len(tail):
            tail.append(v)
        else:
            tail[index] = v

    return len(tail)


# O(n log n)
def longestSubsequenceV3(a, n):
    def ceilIndex(a, l, r, key):
        while r - l > 1:
            m = l + (r - l)//2
            if (a[m] >= key):
                r = m
            else:
                l = m
        return r

    tail = [a[0]]
    for i in range(1, n):
        if a[i] < tail[0]:
            tail[0] = a[i]
        elif a[i] > tail[len(tail)-1]:
            tail.append(a[i])
        else:
            index = ceilIndex(tail, -1, len(tail)-1, a[i])
            tail[index] = a[i]

    return len(tail)


#  O(n^2)
def longestSubsequenceV2(a, n):
    lis = [1] * n
    for i in range(n):
        for j in range(i):
            if a[i] > a[j]:
                lis[i] = max(lis[i], lis[j]+1)

    return max(lis)


def longestSubsequenceV1(a, n):
    class Val:
        def __init__(self, val):
            self.val = val

    def lis(arr, n, maximum):
        if n == 1:
            return 1

        maxEndingHere = 1

        for i in range(1, n):
            res = lis(arr, i, maximum)
            if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
                maxEndingHere = res + 1

        maximum.val = max(maximum.val, maxEndingHere)

        return maxEndingHere

    maximum = Val(1)
    lis(a, n, maximum)

    return maximum.val


if __name__ == '__main__':
    for _ in range(int(input())):
        input()
        n = int(input())
        a = [int(x) for x in input().split()]
        print(longestSubsequence(a, n))
