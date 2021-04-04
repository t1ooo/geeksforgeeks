def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1
    d = 256

    for i in range(M-1):
        h = (h*d) % q

    for i in range(M):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q

    res = []
    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j += 1

            if j == M:
                res.append(i)

        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q
            if t < 0:
                t = t+q

    return res


def searchV2(pat, txt, q):
    M = len(pat)
    N = len(txt)
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1
    d = 256

    for i in range(M-1):
        h = (h*d) % q

    for i in range(M):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q

    res = []
    for i in range(N-M+1):
        if p == t:
            if txt[i:i+M] == pat:
                res.append(i)

        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q
            if t < 0:
                t += q

    return res


# ------------------------
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101
res = [0, 10]

r = search(pat, txt, q)
assert r == res

r = searchV2(pat, txt, q)
assert r == res

# ------------------------
txt = "GEEKS FOR GEEKS"
pat = "ZEEK"
q = 101
res = []

r = search(pat, txt, q)
assert r == res

r = searchV2(pat, txt, q)
assert r == res

# ------------------------
txt = "GEEKS FOR GEEKS"
pat = "geek"
q = 101
res = []

r = search(pat, txt, q)
assert r == res

r = searchV2(pat, txt, q)
assert r == res
