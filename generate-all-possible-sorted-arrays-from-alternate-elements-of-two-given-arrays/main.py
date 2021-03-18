def uniq(arr):
    res = []
    for v in arr:
        if v not in res:
            res.append(v)
    return res


def genV1(a, b):
    def pair(a, b):
        res = []
        for m in a:
            for n in b:
                if m < n:
                    res.append([m, n])

        return res

    def combs(pairs):
        res = pairs.copy()
        for p in pairs:
            res += [(r + p) for r in res if (r[-1] < p[0])]
        return res

    pairs = pair(a, b)
    combPairs = combs(pairs)

    # res = pairs + combinePairs
    # res = uniq(res)
    res = combPairs

    return res


def genV2(A, B):
    def f(A, B, tmp, res):
        # append from A
        if len(tmp) % 2 == 0:
            if len(tmp) > 0:
                res.append(tmp)

            for i in range(len(A)):
                if len(tmp) == 0 or tmp[-1] < A[i]:
                    f(A[i+1:], B, tmp.copy() + [A[i]], res)

        # append from B
        else:
            for i in range(len(B)):
                if tmp[-1] < B[i]:
                    f(A, B[i+1:], tmp.copy() + [B[i]], res)

    res = []
    f(A, B, [], res)

    return res

# ----------------------------------------


def cmparr(a, b):
    return sorted(a) == sorted(b)


a = [10, 15, 25]
b = [1, 5, 20, 30]
r = [
    [10, 20],
    [10, 20, 25, 30],
    [10, 30],
    [15, 20],
    [15, 20, 25, 30],
    [15, 30],
    [25, 30],
]

x = genV1(a, b)
assert cmparr(r, x), x

x = genV2(a, b)
assert cmparr(r, x), x

# ----------------------------------------

a = [10, 15, 25, 35]
b = [1, 5, 20, 30, 40]
r = [
    [10, 20],
    [10, 20, 25, 30],
    [10, 20, 25, 30, 35, 40],
    [10, 20, 25, 40],
    [10, 20, 35, 40],
    [10, 30],
    [10, 30, 35, 40],
    [10, 40],
    [15, 20],
    [15, 20, 25, 30],
    [15, 20, 25, 30, 35, 40],
    [15, 20, 25, 40],
    [15, 20, 35, 40],
    [15, 30],
    [15, 30, 35, 40],
    [15, 40],
    [25, 30],
    [25, 30, 35, 40],
    [25, 40],
    [35, 40],
]

x = genV1(a, b)
assert cmparr(r, x), x

x = genV2(a, b)
assert cmparr(r, x), x

# ----------------------------------------

a = [1, 1, 3, 3]
b = [2, 2, 4, 4]
r = [
    [1, 2],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 4],
    [1, 4],
    [1, 2],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 4],
    [1, 4],
    [3, 4],
    [3, 4],
    [3, 4],
    [3, 4],
]

x = genV1(a, b)
assert cmparr(r, x), x

x = genV2(a, b)
assert cmparr(r, x), x

# ----------------------------------------

a = [1, 2, 3]
b = [1, 2, 3]
r = [
    [1, 2],
    [1, 3],
    [2, 3],
]

x = genV1(a, b)
assert cmparr(r, x), x

x = genV2(a, b)
assert cmparr(r, x), x
