NO_OF_CHARS = 256


def computeTransFun(pat, M, TF):
    lps = 0

    for x in range(NO_OF_CHARS):
        TF[0][x] = 0
    TF[0][ord(pat[0])] = 1

    for i in range(1, M):
        for x in range(NO_OF_CHARS):
            TF[i][x] = TF[lps][x]

        TF[i][ord(pat[i])] = i + 1

        if i < M:
            lps = TF[lps][ord(pat[i])]


def search(pat, txt):
    M = len(pat)
    N = len(txt)
    TF = [[0] * NO_OF_CHARS for _ in range(M + 1)]
    res = []
    computeTransFun(pat, M, TF)

    state = 0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if state == M:
            res.append(i - M + 1)

    return res


txt = "GEEKS FOR GEEKS"
pat = "GEEKS"
assert search(pat, txt) == [0, 10]
