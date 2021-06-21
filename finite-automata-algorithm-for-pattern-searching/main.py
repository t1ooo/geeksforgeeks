from typing import DefaultDict


NO_OF_CHARS = 256


def getNextState(pat, M,  state, x):
    if state < M and x == ord(pat[state]):
        return state + 1

    i = 0
    for ns in range(state, 0, -1):
        if x == ord(pat[ns-1]):
            while i < ns - 1:
                if pat[i] != pat[state - ns + 1 + i]:
                    break
                i += 1
            if i == ns - 1:
                return ns

    return 0


def computeTF(pat, M):
    TF = [[0] * NO_OF_CHARS for _ in range(M+1)]

    for state in range(M+1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, M, state, x)
            TF[state][x] = z

    return TF


def search(pat, txt):
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)
    res = []

    state = 0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if state == M:
            res.append(i - M + 1)

    return res


txt = "AABAACAADAABAAABAA"
pat = "AABA"
assert search(pat, txt) == [0, 9, 13]
