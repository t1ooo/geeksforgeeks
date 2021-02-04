class Solution:
    def minStep(self, n):
        step = 0
        while n > 1:
            if n % 3 == 0:
                n //= 3
            else:
                n -= 1
            step += 1
        return step
