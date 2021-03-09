def findMaxXorV1(arr):
    nums = set([arr[0]])
    for i in range(1, len(arr)):
        nums.update([arr[i] ^ n for n in nums])  # add all elements to set
        nums.add(arr[i])
    return max(nums)


def findMaxXorV2(arr):
    def intToBitArray(num):
        len = 32 - 1
        bits = [int(bit) for bit in "{0:b}".format(num).rjust(len, '0')]
        bits.reverse()
        return bits

    class Node:
        def __init__(self, value=0):
            self.value = value
            self.childs = [None] * 2

    class Trie:
        def __init__(self):
            self.root = Node()

        def insert(self, num):
            curr = self.root
            for bit in intToBitArray(num):
                if curr.childs[bit] == None:
                    curr.childs[bit] = Node()
                curr = curr.childs[bit]

            curr.value = num

        def query(self, num):
            curr = self.root
            for bit in intToBitArray(num):
                oppositeBit = 1 - bit
                if curr.childs[oppositeBit] != None:
                    curr = curr.childs[oppositeBit]

                elif curr.childs[bit] != None:
                    curr = curr.childs[bit]

                else:
                    raise Exception("not found")

            return num ^ curr.value

    res = float("-inf")

    trie = Trie()
    xor = 0
    trie.insert(xor)
    for a in arr:
        xor = xor ^ a
        trie.insert(xor)
        res = max(res, trie.query(xor))

    return res


# ---------------------

def bench(fn, arr, N):
    import time
    name = fn.__name__
    try:
        start = time.time()
        for _ in range(N):
            fn(arr)
        print(name, time.time() - start)
    except Exception as e:
        print(name, e)


arr = [1, 2, 3, 4]
assert findMaxXorV1(arr) == 7
assert findMaxXorV2(arr) == 7

arr = [8, 1, 2, 12, 7, 6]
assert findMaxXorV1(arr) == 15
assert findMaxXorV2(arr) == 15

arr = [4, 6]
assert findMaxXorV1(arr) == 6
assert findMaxXorV2(arr) == 6

arr = [1]
assert findMaxXorV1(arr) == 1
assert findMaxXorV2(arr) == 1


arr = list(range(0, 5000))
N = 1
bench(findMaxXorV1, arr, N)
bench(findMaxXorV2, arr, N)
