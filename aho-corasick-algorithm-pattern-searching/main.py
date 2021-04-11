from collections import deque


def fill(arr, val):
    for i in range(len(arr)):
        arr[i] = val


class AhoCorasickSearch:
    MAXS = 500
    MAXC = 26

    def __init__(self):
        self.out = [None] * self.MAXS
        self.f = [None] * self.MAXS
        self.g = [[None] * self.MAXC for _ in range(self.MAXS)]

    def buildMatchingMachine(self, arr, k):
        fill(self.out, 0)

        for i in range(self.MAXS):
            fill(self.g[i], -1)

        states = 1

        for i in range(k):
            word = arr[i]
            currentState = 0

            for j in range(len(word)):
                ch = ord(word[j]) - ord('a')

                if self.g[currentState][ch] == -1:
                    self.g[currentState][ch] = states
                    states += 1

                currentState = self.g[currentState][ch]

            self.out[currentState] |= 1 << i

        for ch in range(self.MAXC):
            if self.g[0][ch] == -1:
                self.g[0][ch] = 0

        fill(self.f, -1)

        q = deque()

        for ch in range(self.MAXC):
            if self.g[0][ch] != 0:
                self.f[self.g[0][ch]] = 0
                q.append(self.g[0][ch])

        while len(q) > 0:
            state = q.popleft()

            for ch in range(self.MAXC):
                if self.g[state][ch] != -1:
                    failure = self.f[state]

                    while self.g[failure][ch] == -1:
                        failure = self.f[failure]

                    failure = self.g[failure][ch]
                    self.f[self.g[state][ch]] = failure

                    self.out[self.g[state][ch]] |= self.out[failure]

                    q.append(self.g[state][ch])

        return states

    def findNextState(self, currentState, nextInput):
        answer = currentState
        ch = ord(nextInput) - ord('a')

        while self.g[answer][ch] == -1:
            answer = self.f[answer]

        return self.g[answer][ch]

    def searchWords(self, arr, k, text):
        res = {}

        self.buildMatchingMachine(arr, k)
        currentState = 0

        for i in range(len(text)):
            currentState = self.findNextState(currentState, text[i])

            if self.out[currentState] == 0:
                continue

            for j in range(k):
                if self.out[currentState] & (1 << j) > 0:
                    res[arr[j]] = (i - len(arr[j]) + 1, i)

        return res


arr = ["he", "she", "hers", "his"]
text = "ahishers"
k = len(arr)
res = {'his': (1, 3), 'he': (4, 5), 'she': (3, 5), 'hers': (4, 7)}

acs = AhoCorasickSearch()
r = acs.searchWords(arr, k, text)
assert res == r
