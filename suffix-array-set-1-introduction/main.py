class Suffix:
    def __init__(self, index, suff):
        self.index = index
        self.suff = suff

    def __lt__(self, other):
        return self.suff < other.suff


def buildSuffixArray(txt, n):
    suffixes = [Suffix(i, txt[i:]) for i in range(n)]
    suffixes.sort()
    return [s.index for s in suffixes]


def search(pat, txt, suffArr, n):
    m = len(pat)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        res = txt[suffArr[mid]:suffArr[mid]+m]
        if pat == res:
            return suffArr[mid]
        elif res < pat:
            l = mid + 1
        else:
            r = mid - 1

    return -1


txt = "banana"
n = len(txt)

suffArr = buildSuffixArray(txt, n)
assert suffArr == [5, 3, 1, 0, 4, 2]

pat = "nan"
assert search(pat, txt, suffArr, n) == 2
