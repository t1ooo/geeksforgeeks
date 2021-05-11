import functools
from collections import Counter


# Time Limit Exceeded
def solveQueries(nums, queries, k):
    res = [0] * len(queries)
    for i, (l, r) in enumerate(queries):
        d = Counter(nums[l-1:r])
        for count in d.values():
            if k <= count:
                res[i] += 1

    return res


# Time Limit Exceeded
def solveQueriesV2(nums, queries, k):
    d = [dict() for _ in range(len(queries))]
    for n, num in enumerate(nums):
        for i, (l, r) in enumerate(queries):
            if l <= n+1 and n+1 <= r:
                if num not in d[i]:
                    d[i][num] = 0
                d[i][num] += 1

    res = [0] * len(queries)
    for i, v in enumerate(d):
        for num, count in v.items():
            if k <= count:
                res[i] += 1

    return res


def solveQueriesV3(nums, queries, k):
    res = []
    for l, r in queries:
        d = Counter(nums[l-1:r])
        res.append(sum(1 for count in d.values() if k <= count))

    return res


# Time Limit Exceeded
def solveQueriesV4(nums, queries, k):
    cnt = {n: 0 for n in nums}
    answer = [0]
    block = 318

    def compare(x, y):
        x0 = x[0]//block
        y0 = y[0]//block
        if x0 != y0:
            return x0 < y0
        else:
            return x[1] < y[1]

    def add(p, k):
        cnt[nums[p]] += 1
        if cnt[nums[p]] == k:
            answer[0] += 1

    def subtract(p, k):
        cnt[nums[p]] -= 1
        if cnt[nums[p]] == k-1:
            answer[0] -= 1

    q = [(l-1, r-1, i) for i, (l, r) in enumerate(queries)]
    # q.sort(key=lambda x: x[1])
    q.sort(key=functools.cmp_to_key(compare))

    cl, cr = 0, 0
    ans = [0] * len(queries)

    for l, r, i in q:
        while cl < l:
            subtract(cl, k)
            cl += 1
        while cl > l:
            add(cl-1, k)
            cl -= 1
        while cr <= r:
            add(cr, k)
            cr += 1
        while cr > r+1:
            subtract(cr-1, k)
            cr -= 1
        ans[i] = answer[0]

    return ans


class Solution:
    def solveQueries(self, nums, Queries, k):
        # return solveQueries(nums, Queries, k)
        # return solveQueriesV2(nums, Queries, k)
        # return solveQueriesV3(nums, Queries, k)
        return solveQueriesV4(nums, Queries, k)


# ----------------------------
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        input()
        n, q, k = input().split()
        n = int(n)
        q = int(q)
        k = int(k)
        nums = list(map(int, input().split()))
        Queries = []
        for _ in range(q):
            Queries.append(list(map(int, input().split())))
        obj = Solution()
        ans = obj.solveQueries(nums, Queries, k)
        print(*ans)
