#  m: length of string X
#  n: length of string Y
#  X: string X
#  Y: string Y

# use memoization without recursion
def lcs(m, n, X, Y):
    mem = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for k in range(n+1):
            if i == 0 or k == 0:
                mem[i][k] = 0
            elif X[i-1] == Y[k-1]:
                mem[i][k] = 1 + mem[i-1][k-1]
            else:
                mem[i][k] = max(mem[i-1][k], mem[i][k-1])
    return mem[m][n]


# use general memoization
def lcsV3(m, n, X, Y):
    def memoize(func):
        cache = {}

        def funcMem(*args):
            if not args in cache:
                cache[args] = func(*args)
            return cache[args]
        return funcMem

    def lcsSimple(m, n, X, Y):
        if m == 0 or n == 0:
            return 0
        elif X[m-1] == Y[n-1]:
            return 1 + lcsSimple(m-1, n-1, X, Y)
        else:
            return max(lcsSimple(m-1, n, X, Y), lcsSimple(m, n-1, X, Y))

    lcsSimple = memoize(lcsSimple)
    return lcsSimple(m, n, X, Y)


# use memoization
def lcsV2(m, n, X, Y):
    default = -1

    def lcsMem(m, n, X, Y, mem):
        if mem[m][n] != default:
            return mem[m][n]

        ret = default
        if m == 0 or n == 0:
            ret = 0
        elif X[m-1] == Y[n-1]:
            ret = 1 + lcsMem(m-1, n-1, X, Y, mem)
        else:
            ret = max(lcsMem(m-1, n, X, Y, mem), lcsMem(m, n-1, X, Y, mem))

        mem[m][n] = ret
        return ret

    mem = [[default]*(n+1) for i in range(m+1)]
    return lcsMem(m, n, X, Y, mem)


def lcsV1(m, n, X, Y):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(m-1, n-1, X, Y)
    else:
        return max(lcs(m-1, n, X, Y), lcs(m, n-1, X, Y))


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        input()
        m, n = map(int, input().strip().split())
        X = str(input())
        Y = str(input())
        print(lcs(m, n, X, Y))
