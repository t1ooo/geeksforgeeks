def swap(M, row1, row2, col):
    for i in range(col):
        M[row1][i], M[row2][i] = M[row2][i], M[row1][i]


def rank(M):
    R = len(M)
    C = len(M[0])

    rank = C
    for row in range(rank):
        if M[row][row] != 0:
            for col in range(R):
                if col != row:
                    multiplier = (M[col][row] / M[row][row])
                    for i in range(rank):
                        M[col][i] -= multiplier * M[row][i]

        else:
            reduce = True
            for i in range(row+1, R):
                if M[i][row] != 0:
                    swap(M, row, i, rank)
                    reduce = False
                    break

            if reduce:
                rank -= 1
                for i in range(R):
                    M[i][row] = M[i][rank]

            row -= 1

    return rank


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        input()
        M = []
        for _ in range(3):
            M.append([int(v) for v in input().strip().split(" ")])
        print(rank(M))
