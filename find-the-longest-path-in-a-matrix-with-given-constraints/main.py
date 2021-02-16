from copy import deepcopy


def memoize(func):
    cache = {}

    def funcMem(*args):
        key = str(args)
        if not key in cache:
            cache[key] = func(*args)
        return cache[key]
    return funcMem


def maximumPath(N, Matrix):
    def get(Matrix, pos, default):
        x, y = pos
        if x < 0 or y < 0:
            return default
        try:
            return Matrix[x][y]
        except IndexError:
            return default

    def neighbors(pos):
        diffs = [
            (+1,  0),
            (+1, -1),
            (+1, +1),
        ]
        x, y = pos
        return [(x+dx, y+dy) for (dx, dy) in diffs]

    def maxPath(Matrix, pos, dp):
        curr = get(Matrix, pos, None)
        if curr == None:
            return 0

        x, y = pos
        if dp[x][y] != -1:
            return dp[x][y]

        maxSum = 0
        for npos in neighbors(pos):
            maxSum = max(maxSum, curr + maxPath(Matrix, npos, dp))

        dp[x][y] = maxSum
        return maxSum

    maxSum = 0
    dp = [[-1] * N for _ in range(N)]
    for i in range(N):
        pos = (0, i)
        maxSum = max(maxSum, maxPath(Matrix, pos, dp))

    return maxSum


def maximumPathV1(N, Matrix):
    def get(Matrix, pos, default):
        x, y = pos
        if x < 0 or y < 0:
            return default
        try:
            return Matrix[x][y]
        except IndexError:
            return default

    def neighbors(pos):
        diffs = [
            (+1,  0),
            (+1, -1),
            (+1, +1),
        ]
        x, y = pos
        return [(x+dx, y+dy) for (dx, dy) in diffs]

    def maxPath(Matrix, pos, visited):
        curr = get(Matrix, pos, None)
        if curr == None:
            return 0

        if pos in visited:
            return 0

        visited_cp = deepcopy(visited)
        visited_cp.add(pos)

        maxSum = 0
        for npos in neighbors(pos):
            maxSum = max(maxSum, curr + maxPath(Matrix, npos, visited_cp))

        return maxSum

    maxPath = memoize(maxPath)
    row = Matrix[0]
    maxSum = 0
    for i in range(len(row)):
        pos = (0, i)
        visited = set()
        maxSum = max(maxSum, maxPath(Matrix, pos, visited))

    return maxSum

# def maximumPath(self, N, Matrix):
#     def get(Matrix, pos, default):
#         x, y = pos
#         if x < 0 or y < 0:
#             return default
#         try:
#             return Matrix[x][y]
#         except IndexError:
#             return default

#     def maxPath(Matrix, pos, visited, prev):
#         curr = get(Matrix, pos, None)
#         if curr == None:
#             return 0

#         # if curr < prev:
#             # return []

#         if pos in visited:
#             return 0

#         visited_cp = deepcopy(visited)
#         visited_cp.add(pos)

#         diffs = [
#             (+1,  0),
#             (+1, -1),
#             (+1, +1),
#         ]
#         x, y = pos
#         neighbors = [(x+dx, y+dy) for (dx, dy) in diffs]
#         # print(pos, neighbors)

#         # print(curr)

#         # s = curr
#         # s = [curr]
#         # s = [curr] * len(neighbors)
#         # s = [pos]
#         # s = []
#         maxSum = 0
#         for i,npos in enumerate(neighbors):
#             # s += maxPath(Matrix, npos, visited_cp)
#             # s += maxPath(Matrix, npos, visited_cp, curr)
#             # s.append(curr + maxPath(Matrix, npos, visited_cp, curr))
#             maxSum = max(maxSum, curr + maxPath(Matrix, npos, visited_cp, curr))

#         return maxSum

#     # print(Matrix)
#     row = Matrix[0]
#     # maxPaths = []
#     maxSum = 0
#     for i in range(len(row)):
#         prev = 0
#         pos = (0, i)
#         visited = set()
#         # maxPaths.append(maxPath(Matrix, pos, visited, prev))
#         maxSum = max(maxSum, maxPath(Matrix, pos, visited, prev))

#     # print(max(maxPaths))

#     # return max(maxPaths)
#     return maxSum


class Solution:
    def maximumPath(self, N, Matrix):
        return maximumPath(N, Matrix)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr % N] = int(arr[itr])

        ob = Solution()
        print(ob.maximumPath(N, Matrix))
