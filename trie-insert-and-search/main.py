def insert(root, key):
    curr = root
    for ch in key:
        i = charToIndex(ch)
        if curr.children[i] == None:
            curr.children[i] = TrieNode()
        curr = curr.children[i]

    curr.isEndOfWord = True


def search(root, key):
    curr = root
    for ch in key:
        i = charToIndex(ch)
        if curr.children[i] == None:
            return False
        curr = curr.children[i]

    return curr.isEndOfWord


# -----------------------------

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()


# use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch)-ord('a')


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        input()
        n = int(input())
        arr = input().strip().split()
        strs = input()

        t = Trie()
        for s in arr:
            insert(t.root, s)

        if search(t.root, strs):
            print(1)
        else:
            print(0)
