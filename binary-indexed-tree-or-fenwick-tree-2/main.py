def getsum(bittree, i):
    res = 0
    i = i+1
    while i > 0:
        res += bittree[i]
        i -= i & (-i)

    return res


def updatebits(bittree, n, i, v):
    i += 1
    while i <= n:
        bittree[i] += v
        i += i & (-i)


def construct(arr, n):
    bittree = [0] * (n+1)
    for i in range(n):
        updatebits(bittree, n, i, arr[i])

    return bittree


freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]

bittree = construct(freq, len(freq))
assert 12 == getsum(bittree, 5)

freq[3] += 6
updatebits(bittree, len(freq), 3, 6)
assert 18 == getsum(bittree, 5)
