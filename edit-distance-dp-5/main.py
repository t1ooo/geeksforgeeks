def tail(a):
    return a[1:]


def memoize(func):
    cache = {}

    def funcMem(*args):
        if not args in cache:
            cache[args] = func(*args)
        return cache[args]
    return funcMem


# use matrix for memoization and space optimized
def editDistance(s, t):
    ls = len(s)
    lt = len(t)
    m = [[0] * (lt+1) for _ in range(2)]
    flag = True

    for c in range(ls+1):
        flag = not flag
        for d in range(lt+1):
            if c == 0:
                m[flag][d] = d
            elif d == 0:
                m[flag][d] = c
            elif s[c-1] == t[d-1]:
                m[flag][d] = m[not flag][d-1]
            else:
                m[flag][d] = 1 + min(
                    m[not flag][d],
                    m[flag][d-1],
                    m[not flag][d-1]
                )

    return m[flag][lt]


# use matrix for memoization
def editDistanceV3(s, t):
    ls = len(s)
    lt = len(t)
    m = [[0] * (lt+1) for _ in range(ls+1)]

    for c in range(ls+1):
        for d in range(lt+1):
            if c == 0:
                m[c][d] = d
            elif d == 0:
                m[c][d] = c
            elif s[c-1] == t[d-1]:
                m[c][d] = m[c-1][d-1]
            else:
                m[c][d] = 1 + min(
                    m[c-1][d],
                    m[c][d-1],
                    m[c-1][d-1]
                )

    return m[ls][lt]


# use memoization
def editDistanceV2(s, t):
    def distance(s, t):
        if len(s) == 0:
            return len(t)

        if len(t) == 0:
            return len(s)

        if s[0] == t[0]:
            return distance(tail(s), tail(t))

        return 1 + min(
            distance(tail(s), t),
            distance(s, tail(t)),
            distance(tail(s), tail(t)),
        )

    distance = memoize(distance)
    return distance(s, t)


# def editDistance(s, t):
#     def distance(s, t, ls, lt):
#         if ls == 0:
#             return lt

#         if lt == 0:
#             return ls

#         if s[ls-1] == t[lt-1]:
#             return distance(s, t, ls-1, lt-1)

#         return 1 + min(
#             distance(s, t, ls-1, lt),
#             distance(s, t, ls, lt-1),
#             distance(s, t, ls-1, lt-1),
#         )

#     distance = memoize(distance)
#     return distance(s, t, len(s), len(t))


# simple
def editDistanceV1(s, t):
    def distance(s, t):
        if len(s) == 0:
            return len(t)

        if len(t) == 0:
            return len(s)

        if s[0] == t[0]:
            return distance(tail(s), tail(t))

        return 1 + min(
            distance(tail(s), t),       # insert
            distance(s, tail(t)),       # delete
            distance(tail(s), tail(t)),  # replace
        )

    return distance(s, t)


class Solution:
    def editDistance(self, s, t):
        return editDistance(s, t)


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        input()
        # print(i)
        s, t = input().split(" ")
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)
