def countWays(N, S):
    def countParenth(symb, oper, n):
        F = [[0] * (n + 1) for _ in range(n + 1)]
        T = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            if symb[i] == 'T':
                T[i][i] = 1
                F[i][i] = 0
            else:
                T[i][i] = 0
                F[i][i] = 1

        for gap in range(1, n):
            i = 0
            for j in range(gap, n):
                trueIJ = 0
                falseIJ = 0
                for g in range(gap):
                    k = i + g

                    trueIK = T[i][k]
                    trueK1J = T[k + 1][j]

                    falseIK = F[i][k]
                    falseK1J = F[k + 1][j]

                    op = oper[k]
                    if op == '&':
                        tmp = trueIK * trueK1J
                        tmp2 = (trueIK + falseIK) * (trueK1J + falseK1J)
                        trueIJ += tmp
                        falseIJ += (tmp2 - tmp)

                    elif op == '|':
                        tmp = falseIK * falseK1J
                        tmp2 = (trueIK + falseIK) * (trueK1J + falseK1J)
                        trueIJ += (tmp2 - tmp)
                        falseIJ += tmp

                    elif op == '^':
                        trueIJ += (falseIK * trueK1J + trueIK * falseK1J)
                        falseIJ += (trueIK * trueK1J + falseIK * falseK1J)

                T[i][j] = trueIJ
                F[i][j] = falseIJ
                i += 1

        return T[0][n - 1]

    symb = []
    oper = []
    for i in range(N):
        if i % 2 == 0:
            symb.append(S[i])
        else:
            oper.append(S[i])

    return countParenth(symb, oper, len(symb)) % 1003


def countWaysV2(N, S):
    def split(s):
        res = []
        i = 0
        while i+2 < len(s):
            res.append([s[0:i+1], s[i+1:i+2], s[i+2:]])
            i += 2
        return res

    def f(s, dp):
        if len(s) == 1:
            if s == "T":
                return (1, 0)
            else:
                return (0, 1)

        if s in dp:
            return dp[s]

        leftRes, rightRes = 0, 0
        for l, op, r in split(s):
            leftTrue, leftFalse = f(l, dp)
            rightTrue, rightFalse = f(r, dp)

            if op == "&":
                leftRes += leftTrue*rightTrue

                rightRes += (leftTrue*rightFalse +
                             leftFalse*rightTrue +
                             leftFalse*rightFalse)

            elif op == "^":
                leftRes += (leftTrue*rightFalse +
                            leftFalse*rightTrue)

                rightRes += (leftTrue*rightTrue +
                             leftFalse*rightFalse)

            elif op == "|":
                leftRes += (leftTrue*rightFalse +
                            leftFalse*rightTrue +
                            leftTrue*rightTrue)

                rightRes += leftFalse*rightFalse

            else:
                raise Exception("invalid op")

        dp[s] = (leftRes, rightRes)
        return dp[s]

    dp = {}
    return f(S, dp)[0] % 1003


def countWaysV1(N, S):
    T = True
    F = False

    def boot2str(b):
        return str(b)[0]

    exprDict = {
        "T": boot2str(T),
        "F": boot2str(F),

        "T&T": boot2str(T & T),
        "T^T": boot2str(T ^ T),
        "T|T": boot2str(T | T),

        "F&F": boot2str(F & F),
        "F^F": boot2str(F ^ F),
        "F|F": boot2str(F | F),

        "T&F": boot2str(T & F),
        "T^F": boot2str(T ^ F),
        "T|F": boot2str(T | F),

        "F&T": boot2str(F & T),
        "F^T": boot2str(F ^ T),
        "F|T": boot2str(F | T),
    }

    def split(s):
        i = 0
        while i+2 < len(s):
            yield s[0:i+1], s[i+1:i+2], s[i+2:]
            i += 2

    def f(s, dp):
        if len(s) <= 3:
            return exprDict[s]

        if s in dp:
            return dp[s]

        res = []
        for l, op, r in split(s):
            for ll in f(l, dp):
                for rr in f(r, dp):
                    res.append(f(ll + op + rr, dp))

        dp[s] = res
        return res

    dp = {}
    return f(S, dp).count("T") % 1003


class Solution:
    def countWays(self, N, S):
        return countWays(N, S)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        S = input()

        ob = Solution()
        print(ob.countWays(N, S))
        # for _ in range(10000):
            # ob.countWays(N, S)
