N = 4  # number of men|women


def wPrefersCurrOverOther(prefer, w, currM, otherM):
    for m in prefer[w]:
        if m == currM:
            return True

        if m == otherM:
            return False

    return False


def findFreeM(freeM):
    m = 0
    for m in range(N):
        if freeM[m] == False:
            return m
    return -1


def stableMarriage(prefer):
    freeM = [False] * N  # free man
    partnerW = [-1] * N  # partners of woman
    freeCount = N

    while freeCount > 0:
        m = findFreeM(freeM)

        for w in prefer[m]:
            if freeM[m] != False:
                break

            i = w - N
            if partnerW[i] == -1:
                partnerW[i] = m
                freeM[m] = True
                freeCount -= 1
            else:
                currM = partnerW[i]
                if wPrefersCurrOverOther(prefer, w, currM, m) == False:
                    partnerW[i] = m
                    freeM[m] = True
                    freeM[currM] = False

    res = []
    for i in range(N):
        res.append([i + N, partnerW[i]])

    return res


prefer = [[7, 5, 6, 4], [5, 4, 6, 7],
          [4, 5, 6, 7], [4, 5, 6, 7],
          [0, 1, 2, 3], [0, 1, 2, 3],
          [0, 1, 2, 3], [0, 1, 2, 3]]

assert stableMarriage(prefer) == [[4, 2], [5, 1], [6, 3], [7, 0]]
