# Time Limit Exceeded
def lpsV1(s):
    l = 1
    r = len(s)-1
    while r > 0:
        if s[:r] == s[l:]:
            break
        r -= 1
        l += 1
    return r


# Time Limit Exceeded
def lpsV2(s):
    res = 0
    for i in range(1, len(s)):
        if s[:i] == s[-i:]:
            res = i
    return res


# simple search algo
def lpsV3(s):
    l = 0
    offset = 1
    r = offset
    while r < len(s):
        if s[l] == s[r]:
            l += 1
            r += 1
        else:
            l = 0
            offset += 1
            r = offset

    return l


def lpsV4(s):
    n = len(s)
    lps = [0] * n
    l = 0
    r = 1
    while r < n:
        if s[r] == s[l]:
            l += 1
            lps[r] = l
            r += 1
        else:
            if l == 0:
                lps[r] = 0  # ?
                r += 1
            else:
                l = lps[l-1]

    return lps[-1]


def lpsV5(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]

        while k > 0 and s[k] != s[i]:
            k = p[k-1]

        if s[k] == s[i]:
            k += 1

        p[i] = k

    # print(list(map(str, p)))
    # print(list(s))
    return p[-1]


class Solution:
    def lps(self, s):
        # return lpsV1(s)
        # return lpsV2(s)
        # return lpsV3(s)
        # return lpsV4(s)
        return lpsV5(s)


# ----------------
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        input()
        s = input()
        ob = Solution()
        answer = ob.lps(s)
        print(answer)
