import random
import main
import time
import traceback


def bench(fn, n, N):
    try:
        start = time.time()
        for _ in range(N):
            fn(n)
        print(fn.__name__, time.time() - start)
    except Exception as e:
        print(fn.__name__, e)


if __name__ == "__main__":
    N = 10
    
    n = 100000
    print(n)
    bench(main.sieveV1, n, N)
    bench(main.sieveV2, n, N)
    bench(main.sieveV3, n, N)
    bench(main.sieveV4, n, N)
    print("----------------------")
