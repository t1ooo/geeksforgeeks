import main


def test(binarySearchFunc):
    import random

    for _ in range(1000):
        arr = []
        n = 0
        for i in range(random.randrange(1, 100)):
            n += random.randrange(1, 100)
            arr.append(n)

        N = len(arr)
        for i in range(N):
            ii = binarySearchFunc(arr, 0, N-1, arr[i])
            if i != ii:
                raise Exception(f"{i} != {ii}")

    print(binarySearchFunc.__name__, ": ok")


test(main.binarySearchRec)
test(main.binarySearch)
