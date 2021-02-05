from copy import deepcopy


class Solution:
    def find_distances(self, m):
        dist = deepcopy(m)
        V = len(dist)
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        print("dbg:", i, j, "|", i, k, "|", k, j, "|",
                              dist[i][j], dist[i][k], dist[k][j])
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist


def format(n):
    if n == 10000000:
        return "INF"
    return str(n)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        tt = int(input())
        m = []
        for _ in range(tt):
            s = [int(x) for x in input().strip().split(" ")]
            m.append(s)
        ob = Solution()
        ans = ob.find_distances(m)
        for v in ans:
            print(" ".join([format(x) for x in v]))
