import random
import main
import time
import traceback


def bench(fn, arr, N):
    try:
        start = time.time()
        for _ in range(N):
            res = arr.copy()
            low = 0
            high = len(res) - 1
            fn(arr, low, high)
        print(fn.__name__, time.time() - start)
    except Exception as e:
        print(fn.__name__, e)


if __name__ == "__main__":
    N = 10
    arr = []
    for i in range(1000):
        arr.append(random.randint(1, 1000))

    print(len(arr))
    bench(main.quickSortV5, arr, N)
    bench(main.quickSortV4, arr, N)
    bench(main.quickSortV3, arr, N)
    bench(main.quickSortV2, arr, N)
    bench(main.quickSortV1, arr, N)
    print("----------------------")

    N = 10
    arr = []
    for i in range(1000):
        arr.append(i)

    print(len(arr), "sorted")
    bench(main.quickSortV5, arr, N)
    bench(main.quickSortV4, arr, N)
    bench(main.quickSortV3, arr, N)
    bench(main.quickSortV2, arr, N)
    bench(main.quickSortV1, arr, N)
    print("----------------------")

    N = 1
    arr = []
    for i in range(100000):
        arr.append(random.randint(1, 1000))

    print(len(arr))
    bench(main.quickSortV5, arr, N)
    bench(main.quickSortV4, arr, N)
    bench(main.quickSortV3, arr, N)
    bench(main.quickSortV2, arr, N)
    bench(main.quickSortV1, arr, N)
    print("----------------------")
