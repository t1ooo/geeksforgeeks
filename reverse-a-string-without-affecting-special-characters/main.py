def if_special_char(ch):
    return not ch.isdigit() and not ch.isalpha()


def swap(arr, i, k):
    arr[i], arr[k] = arr[k], arr[i]


class Solution:
    def reverse(self, s):
        ls = list(s)
        l = 0
        r = len(ls) - 1
        while l < r:
            if if_special_char(ls[l]):
                l += 1
            elif if_special_char(ls[r]):
                r -= 1
            else:
                swap(ls, l, r)
                l += 1
                r -= 1

        return ''.join(ls)


# -----------------------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        s = input().strip()
        ob = Solution()
        ans = ob.reverse(s)
        print(ans)
