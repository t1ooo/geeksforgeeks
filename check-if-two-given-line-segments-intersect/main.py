x = 0
y = 1


def onSegment(p, q, r):
    return (
        q[x] <= max(p[x], r[x]) and q[x] >= min(p[x], r[x]) and
        q[y] <= max(p[y], r[y]) and q[y] >= min(p[y], r[y])
    )


def orientation(p, q, r):
    val = (q[y] - p[y]) * (r[x] - q[x]) - \
          (q[x] - p[x]) * (r[y] - q[y])
    if val > 0:
        return 1
    if val < 0:
        return 2
    return 0


def doIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and onSegment(p1, p2, q1):
        return True
    if o2 == 0 and onSegment(p1, q2, q1):
        return True
    if o3 == 0 and onSegment(p2, p1, q2):
        return True
    if o4 == 0 and onSegment(p2, q1, q2):
        return True

    return False


class Solution:
    def doIntersect(self, p1, q1, p2, q2):
        return int(doIntersect(p1, q1, p2, q2))


# ---------------------------
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        input()
        S1 = list(map(int, input().strip().split(" ")))
        S2 = list(map(int, input().strip().split(" ")))
        p1 = []
        q1 = []
        p2 = []
        q2 = []
        p1.append(S1[0])
        p1.append(S1[1])
        q1.append(S1[2])
        q1.append(S1[3])
        p2.append(S2[0])
        p2.append(S2[1])
        q2.append(S2[2])
        q2.append(S2[3])
        ob = Solution()
        ans = ob.doIntersect(p1, q1, p2, q2)
        print(ans)
