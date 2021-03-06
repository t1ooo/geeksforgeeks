def findConvexHullV1(points):
    def findLeftIndex(points):
        x = 0
        y = 1
        minI = 0
        for i in range(1, len(points)):
            if points[i][x] < points[minI][x]:
                minI = i
            elif points[i][x] == points[minI][x]:
                if points[i][y] < points[minI][y]:
                    minI = i
        return minI

    def orientation(a, b, c):
        x = 0
        y = 1
        v = (b[y] - a[y]) * (c[x] - b[x]) - \
            (b[x] - a[x]) * (c[y] - b[y])
        if v == 0:
            return 0
        elif v > 0:
            return 1
        else:
            return 2

    if len(points) < 3:
        return [[-1]]

    points.sort()

    res = []
    left = findLeftIndex(points)

    p = left
    q = 0
    while True:
        res.append(points[p])
        q = (p+1) % len(points)
        for i in range(len(points)):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        if p == left:
            break

    res.sort()

    return res


def findConvexHullV2(points):
    COLLINEAR = 0
    CLOCK = 1
    COUNTERCLOCKWISE = 2
    X = 0
    Y = 1

    def findLeftIndex(points):
        minI = 0
        for i in range(1, len(points)):
            if points[i][X] < points[minI][X]:
                minI = i
        return minI

    def orientation(a, b, c):
        v = (b[Y] - a[Y]) * (c[X] - b[X]) - \
            (b[X] - a[X]) * (c[Y] - b[Y])
        if v == 0:
            return COLLINEAR
        elif v > 0:
            return CLOCK
        else:
            return COUNTERCLOCKWISE

    def nextPoint(a, points):
        c = (a+1) % len(points)
        for b in range(len(points)):
            if orientation(points[a], points[b], points[c]) == COUNTERCLOCKWISE:
                c = b
        return c

    if len(points) < 3:
        return [[-1]]

    points.sort()

    res = []
    left = findLeftIndex(points)
    a = left
    while True:
        res.append(points[a])
        a = nextPoint(a, points)
        if a == left:
            break

    res.sort()
    return res


class Solution:
    def FindConvexHull(self, points):
        # return findConvexHullV1(points)
        return findConvexHullV2(points)


# ----------------------


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        input()
        n = int(input())
        points_list = []
        for _ in range(n):
            points_list.append(list(map(int, input().split())))
        obj = Solution()
        ans = obj.FindConvexHull(points_list)
        for v in ans:
            print(v, end=" ")
        print()
