def if_special_char(ch):
    return not ch.isdigit() and not ch.isalpha()


class Solution:
    def reverse(self, s):
        ls = list(s)
        l = 0
        r = len(ls) - 1
        while l < r:
            if if_special_char(ls[l]):
                l += 1
                continue
            if if_special_char(ls[r]):
                r -= 1
                continue
            ls[l], ls[r] = ls[r], ls[l]
            l += 1
            r -= 1
        return ''.join(ls)
