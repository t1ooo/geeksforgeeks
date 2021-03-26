def stockBuySellV1(price, n):
    if n == 1:
        return []

    res = []
    i = 0
    while i < n-1:
        while (i < n-1) and (price[i+1] <= price[i]):
            i += 1

        if i == n-1:
            break

        buy = i

        i += 1
        while (i < n) and (price[i-1] < price[i]):
            i += 1

        sell = i-1

        res.append([buy, sell])

    return res


def stockBuySellV2(price, n):
    if n == 1:
        return []

    res = []
    i = 1
    while i < n:
        while i < n and price[i-1] > price[i]:
            i+=1
            continue
        
        if not i < n:
            break

        buy = i-1

        while i < n and price[i-1] < price[i]:
            i+=1
            continue

        sell = i-1
        i+=1

        res.append([buy, sell])

    return res


class Solution:
    def stockBuySell(self, A, n):
        # return stockBuySellV1(A, n)
        return stockBuySellV2(A, n)


# ------------------------------
def check(ans, A, p):
    c = 0
    for i in range(len(ans)):
        c += A[ans[i][1]]-A[ans[i][0]]
    # print(c, p)
    if(c == p):
        return 1
    else:
        return 0


# ---------------------------
if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        input()
        n = int(input())
        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        ans = ob.stockBuySell(A, n)
        p = 0
        for i in range(n-1):
            p += max(0, A[i+1]-A[i])
        if(len(ans) == 0):
            print("No Profit", end="")
        else:
            print(check(ans, A, p), end="")
        print()
        t -= 1
