from math import log2

MAX = 500

lookup = [[0] * MAX for _ in range(MAX)]


class Query:
    def __init__(self, l, r):
        self.L = l
        self.R = r


def preprocess(arr, n):
    global lookup

    for i in range(n):
        lookup[i][0] = i

    j = 1
    while (2 ** j) <= n:
        i = 0
        while i + (2 ** j) - 1 < n:
            a = lookup[i][j - 1]
            b = lookup[i + (2 ** (j - 1))][j - 1]
            if arr[a] < arr[b]:
                lookup[i][j] = a
            else:
                lookup[i][j] = b
            i += 1

        j += 1


def query(arr, L, R):
    global lookup

    j = int(log2(R - L + 1))

    a = lookup[L][j]
    b = lookup[R - (2 ** j) + 1][j]
    return min(arr[a], arr[b])


def RMQ(arr, n, q, m):
    preprocess(arr, n)
    res = []
    for i in range(m):
        L = q[i].L
        R = q[i].R
        res.append(query(arr, L, R))
    return res


# -------------------------------------
a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
n = len(a)
q = [Query(0, 4), Query(4, 7), Query(7, 8)]
m = len(q)

assert RMQ(a, n, q, m) == [0, 3, 12]


# -------------------------------------
a = [0, 5, 2, 5, 4, 3, 1, 6, 3]
n = len(a)
q = [Query(3, 8)]
m = len(q)

assert RMQ(a, n, q, m) == [1]
