from copy import deepcopy


class Solution:
    def wordBoggle(self, board, dictionary):
        return [word
                for word in dictionary
                if self.contains(board, word)]

    def contains(self, board, word):
        for i, row in enumerate(board):
            for k, _ in enumerate(row):
                pos = (i, k)
                visited = set()
                if self.findChars(board, word, pos, visited):
                    return True

        return False

    def findChars(self, board, word, pos, visited):
        if len(word) == 0:
            return True

        if word[0] != self.get(board, pos, None):
            return False

        if pos in visited:
            return False

        visited_copy = deepcopy(visited)
        visited_copy.add(pos)

        for n_pos in self.genNeighbors(pos):
            if self.findChars(board, word[1:], n_pos, visited_copy):
                return True

        return False

    def genNeighbors(self, pos):
        diffs = [
            (1, 0), (-1, 0),   # |
            (0, 1), (0, -1),   # --
            (-1, -1), (1, 1),  # \
            (-1, 1), (1, -1),  # /
        ]
        i, k = pos
        return [(i + di, k + dk)
                for di, dk in diffs]

    def get(self, board, pos, default):
        i, k = pos
        if i < 0 or k < 0:
            return default

        try:
            return board[i][k]
        except IndexError:
            return default


class SolutionV1:
    def wordBoggle(self, board, dictionary):
        found_words = []
        for word in dictionary:
            if self.contains(board, word):
                found_words.append(word)
        return found_words

    def contains(self, board, word):
        if len(word) == 0:
            return True

        start_positions = self.findStartPositions(board, word[0])
        if len(start_positions) == 0:
            return False

        for pos in start_positions:
            visited = set()
            visited.add(pos)
            if self.findChars(board, word[1:], pos, visited):
                return True

        return False

    def findStartPositions(self, board, char):
        start_positions = []
        for i, row in enumerate(board):
            for k, r_char in enumerate(row):
                if char == r_char:
                    start_positions.append((i, k))
        return start_positions

    def findChars(self, board, word, pos, visited):
        if len(word) == 0:
            return True

        char = word[0]
        for n_pos in self.genNeighbors(pos):
            if n_pos in visited:
                continue
            b_char = self.get(board, n_pos, None)
            if char == b_char:
                visited_copy = deepcopy(visited)
                visited_copy.add(n_pos)
                if self.findChars(board, word[1:], n_pos, visited_copy):
                    return True

        return False

    def genNeighbors(self, pos):
        diffs = [
            (1, 0), (-1, 0),  # |
            (0, 1), (0, -1),  # --
            (-1, -1), (1, 1),  # \
            (-1, 1), (1, -1),  # /
        ]
        neighbors = []
        for diff in diffs:
            neighbors.append((pos[0] + diff[0], pos[1] + diff[1]))
        return neighbors

    def get(self, board, pos, default):
        i, k = pos
        if i < 0 or k < 0:
            return default
        try:
            return board[i][k]
        except IndexError:
            return default


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        dictionary = [x for x in input().strip().split()]
        line = input().strip().split()

        R = int(line[0])
        C = int(line[1])

        board = []
        for _ in range(R):
            board.append([x for x in input().strip().split()])

        obj = Solution()
        found = obj.wordBoggle(board, dictionary)
        if len(found) == 0:
            print(-1)
        else:
            found.sort()
            for i in found:
                print(i)
