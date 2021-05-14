import functools


def convexHullV1(points):
    X = 0
    Y = 1
    COLINEAR = 0
    CLOCK = 1
    COUNTERCLOCK = 2
    p0 = (None, None)
    n = len(points)

    def distanceSquare(p1, p2):
        return ((p1[X] - p2[X]) ** 2) + ((p1[Y] - p2[Y]) ** 2)

    def orientation(p, q, r):
        v = (q[Y] - p[Y]) * (r[X] - q[X]) - \
            (q[X] - p[X]) * (r[Y] - q[Y])
        if v == 0:
            return COLINEAR
        elif v > 0:
            return CLOCK
        else:
            return COUNTERCLOCK

    def compare(p1, p2):
        o = orientation(p0, p1, p2)
        if o == COLINEAR:
            if distanceSquare(p0, p2) >= distanceSquare(p0, p1):
                return -1
            else:
                return 1

        if o == COUNTERCLOCK:
            return -1
        else:
            return 1

    ymin = min(points, key=lambda p: (p[Y], p[X]))
    i = points.index(ymin)

    points[0], points[i] = points[i], points[0]
    p0 = points[0]

    points = [p0] + sorted(points[1:], key=functools.cmp_to_key(compare))

    m = 1
    i = 1
    while i < n:
        while i < n-1 and orientation(p0, points[i], points[i+1]) == COLINEAR:
            i += 1
        points[m] = points[i]
        m += 1
        i += 1

    if m < 3:
        return [[-1]]

    s = []
    s.append(points[0])
    s.append(points[1])
    s.append(points[2])

    i = 3
    while i < m:
        while len(s) > 1 and orientation(s[-2], s[-1], points[i]) != COUNTERCLOCK:
            s.pop()
        s.append(points[i])
        i += 1

    s.sort()
    return s


class Solution:
    def FindConvexHull(self, points):
        return convexHullV1(points)


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
        # if(len(ans) == 1):
        #     for _ in ans[0]:
        #         print(_, end=" ")
        #     print()
        # else:
        #     for _ in ans:
        #         for __ in _:
        #             print(__, end=" ")
        #         print()
