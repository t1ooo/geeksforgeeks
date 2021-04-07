def search(text, pattern):
    def zArray(string):
        n = len(string)
        z = [0] * n

        l, r, k = 0, 0, 0
        for i in range(1, n):
            if i > r:
                l, r = i, i
                while r < n and string[r-l] == string[r]:
                    r += 1

                z[i] = r-l
                r -= 1
            else:
                k = i-l

                if z[k] < r-i+1:
                    z[i] = z[k]
                else:
                    l = i
                    while r < n and string[r-l] == string[r]:
                        r += 1

                    z[i] = r-l
                    r -= 1

        return z

    concat = pattern+"$"+text
    l = len(concat)
    z = zArray(concat)
    # print(list(concat))
    # print(list(map(str, z)))
    res = []
    for i in range(l):
        if z[i] == len(pattern):
            res.append(i-len(pattern)-1)

    return res


def searchV2(text, pattern):
    def zArray(s):
        n = len(s)
        zf = [0] * n
        left = 0
        right = 0
        for i in range(1, n):
            zf[i] = max(0, min(right-i, zf[i-left]))
            while i+zf[i] < n and s[zf[i]] == s[i+zf[i]]:
                zf[i] += 1
            if i+zf[i] > right:
                left = i
                right = i+zf[i]

        return zf

    concat = pattern+"$"+text
    l = len(concat)
    z = zArray(concat)
    # print(list(concat))
    # print(list(map(str, z)))
    res = []
    for i in range(l):
        if z[i] == len(pattern):
            res.append(i-len(pattern)-1)

    return res


text = "GEEKS FOR GEEKS"
pattern = "GEEKS"
r = [0, 10]

assert r == search(text, pattern)
assert r == searchV2(text, pattern)
