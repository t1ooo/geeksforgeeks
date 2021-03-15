def isPalindrome(s):
    rev = s[::-1]
    return s == rev


def allPalindromicPartitionsV1(str):
    def f(str, l, r, tmp, res):
        if l > r:
            res.append(tmp.copy())
            return

        for k in range(l, r+1):
            s = str[l:k+1]
            if isPalindrome(s):
                tmp.append(s)
                f(str, k+1, r, tmp, res)
                tmp.pop()

    res = []
    f(str, 0, len(str)-1, [], res)
    return res


def allPalindromicPartitionsV2(str):
    def f(str, tmp, res):
        if len(str) == 0:
            res.append(tmp.copy())
            return

        for k in range(len(str)):
            s = str[0:k+1]
            if isPalindrome(s):
                tmp.append(s)
                f(str[k+1:], tmp, res)
                tmp.pop()

    res = []
    f(str, [], res)
    return res


def allPalindromicPartitionsV3(str):
    def f(s):
        res = []
        for i in range(len(s)-1):
            left = s[:i+1]
            if isPalindrome(left):
                right = s[i+1:]
                for next in f(right):
                    res.append(left + " " + next)

        if isPalindrome(s):
            res.append(s)

        return res

    return [v.split(" ") for v in f(str)]


def solution(str):
    # return allPalindromicPartitionsV1(str)
    # return allPalindromicPartitionsV2(str)
    return allPalindromicPartitionsV3(str)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        input()
        str = input()
        res = solution(str)
        for r in res:
            print(*r, end="; ")
        print()
