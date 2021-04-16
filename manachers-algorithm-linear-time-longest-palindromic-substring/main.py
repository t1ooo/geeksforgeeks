def findLongestPalindromV1(S):
    def updatedString(S):
        buf = ["#"]
        for ch in S:
            buf.append(ch)
            buf.append("#")
        return "".join(buf)

    S = updatedString(S)
    LPS = [0] * len(S)
    C = 0
    R = 0
    for i in range(len(S)):
        if R > i:
            iMirror = (2*C)-i
            LPS[i] = min(R-i, LPS[iMirror])
        # else:
            # LPS[i] = 0

        try:
            while S[i+(1+LPS[i])] == S[i-(1+LPS[i])]:
                LPS[i] += 1
        except:
            pass

        if i+LPS[i] > R:
            C = i
            R = i+LPS[i]

    r = max(LPS)
    c = LPS.index(r)
    return S[c-r:c+r].replace("#", "")


class Solution:
    def longestPalin(self, S):
        return findLongestPalindromV1(S)


# -----------------------------------
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        input()
        S = input()
        solObj = Solution()
        ans = solObj.longestPalin(S)
        print(ans)
