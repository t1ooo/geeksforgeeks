import math


def build(t, a, v, tl, tr):
    if tl == tr:
        t[v] = a[tl]
    else:
        tm = (tl+tr) // 2
        build(t, a, v*2, tl, tm)
        build(t, a, (v*2)+1, tm+1, tr)
        t[v] = t[v*2] + t[(v*2)+1]


def sum(t, v, tl, tr, l, r):
    if l > r:
        return 0

    if l == tl and r == tr:
        return t[v]

    tm = (tl+tr) // 2
    return (
        sum(t, v*2, tl, tm, l, min(r, tm)) +
        sum(t, (v*2)+1, tm+1, tr, max(l, tm+1), r)
    )


def update(t, v, tl, tr, pos, newval):
    if tl == tr:
        t[v] = newval
    else:
        tm = (tl+tr) // 2
        if pos <= tm:
            update(t, v*2, tl, tm, pos, newval)
        else:
            update(t, (v*2)+1, tm+1, tr, pos, newval)

        t[v] = t[v*2] + t[(v*2)+1]


a = [1, 3, 5, 7, 9, 11]
n = len(a)

x = int(math.ceil(math.log2(n)))
max_size = 2 * (2**x)

t = [0] * max_size
build(t, a, 1, 0, n-1)
# print(t)
assert 15 == sum(t, 1, 0, n-1, 1, 3)

update(t, 1, 0, n-1, 1, 10)
assert 22 == sum(t, 1, 0, n-1, 1, 3)


# ----------------------------------

def buildIterative(t, a, n):
    for i in range(n):
        t[n + i] = a[i]

    # for i in range(n-1, 0, -1):
    for i in reversed(range(1, n)):
        t[i] = t[2*i] + t[(2*i)+1]


def sumIterative(t, l, r, n):
    res = 0
    l += n
    r += n + 1
    while l < r:
        if l & 1:
            res += t[l]
            l += 1
        if r & 1:
            r -= 1
            res += t[r]
        l //= 2
        r //= 2

    return res


def updateIterative(t, id, val, n):
    id += n
    t[id] = val

    while id > 1:
        id //= 2
        t[id] = t[2*id] + t[(2*id)+1]


a = [1, 3, 5, 7, 9, 11]
n = len(a)

max_size = n*2

t = [0] * max_size
buildIterative(t, a, n)
# print(t)
assert 15 == sumIterative(t, 1, 3, n)

updateIterative(t, 1, 10, n)
assert 22 == sumIterative(t, 1, 3, n)
