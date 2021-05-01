def gaussianEliminationV1(mat):
    N = 3

    def gaussianElimination(mat):

        singular_flag = forwardElim(mat)

        if singular_flag != -1:
            print("Singular Matrix.")

            if mat[singular_flag][N] != 0:
                print("Inconsistent System.")
            else:
                print("May have infinitely many solutions.")

            return

        backSub(mat)

    def swap_row(mat, i, j):
        for k in range(N+1):
            mat[i][k], mat[j][k] = mat[j][k], mat[i][k]

    def forwardElim(mat):
        for k in range(N):

            i_max = k
            v_max = mat[i_max][k]

            for i in range(k+1, N):
                if abs(mat[i][k]) > v_max:
                    v_max = mat[i][k]
                    i_max = i

            if mat[k][i_max] == 0:
                return k

            if i_max != k:
                swap_row(mat, k, i_max)

            for i in range(k+1, N):

                f = mat[i][k] / mat[k][k]

                for j in range(k+1, N+1):
                    mat[i][j] -= mat[k][j] * f

                mat[i][k] = 0

        return -1

    def backSub(mat):
        x = [0] * N
        for i in reversed(range(0, N)):
            x[i] = mat[i][N]

            for j in range(i+1, N):
                x[i] -= mat[i][j] * x[j]

            x[i] = x[i] / mat[i][i]

        print(x)

    gaussianElimination(mat)


# from https://cp-algorithms.com/linear_algebra/linear-system-gauss.html
def gaussianEliminationV2(a, ans):
    EPS = 1e-9
    INF = 2

    n = len(a)
    m = len(a[0]) - 1

    where = [-1] * m
    col = -1
    row = 0
    while col < m and row < n:
        col += 1

        sel = row
        for i in range(row, n):
            if abs(a[i][col]) > abs(a[sel][col]):
                sel = i

        if abs(a[sel][col]) < EPS:
            continue

        for i in range(col, m+1):
            a[sel][i], a[row][i] = a[row][i], a[sel][i]

        where[col] = row

        for i in range(n):
            if i != row:
                c = a[i][col] / a[row][col]
                for j in range(col, m+1):
                    a[i][j] -= a[row][j] * c

        row += 1

    for i in range(0, m):
        if where[i] != - 1:
            ans[i] = a[where[i]][m] / a[where[i]][i]

    for i in range(n):
        sum = 0

        for i in range(j, m):
            sum += ans[j] * a[i][j]

        if abs(sum-a[i][m]) > EPS:
            return 0

    for i in range(m):
        if where[i] == -1:
            return INF

    return 1


mat = [[3.0,  2.0, -4.0, 3.0],
       [2.0,  3.0,  3.0, 15.0],
       [5.0, -3.0,  1.0, 14.0]]

gaussianEliminationV1(mat.copy())

ans = [0] * 3
gaussianEliminationV2(mat.copy(), ans)
print(ans)
