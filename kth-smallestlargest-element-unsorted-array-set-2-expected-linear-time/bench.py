import random
import main
import time


# def bench(fn, arr, N, ki):
#     try:
#         start = time.time()
#         for _ in range(N):
#             res = arr.copy()
#             l = 0
#             r = len(res) - 1
#             k = res[ki]
#             fn(arr, l, r, k)
#         print(fn.__name__, time.time() - start)
#     except Exception as e:
#         print(fn.__name__, e)


# if __name__ == "__main__":
#     N = 10
#     arr = []
#     ln = 1000
#     for i in range(ln):
#         arr.append(random.randint(1, 1000))

#     for ki in [0, ln//2, ln-1]:
#         print(ln, ki)
#         bench(main.kthSmallestV8, arr, N, ki)
#         bench(main.kthSmallestV7, arr, N, ki)
#         bench(main.kthSmallestV6, arr, N, ki)
#         bench(main.kthSmallestV5, arr, N, ki)
#         bench(main.kthSmallestV4, arr, N, ki)
#         bench(main.kthSmallestV3, arr, N, ki)
#         bench(main.kthSmallestV2, arr, N, ki)
#         bench(main.kthSmallestV1, arr, N, ki)
#         print("----------------------")





# def bench(fn, arr, N, kis):
#     try:
#         start = time.time()
#         for _ in range(N):
#             for ki in kis:
#                 res = arr.copy()
#                 l = 0
#                 r = len(res) - 1
#                 k = res[ki]
#                 fn(arr, l, r, k)
#         print(fn.__name__, time.time() - start)
#     except Exception as e:
#         print(fn.__name__, e)


# if __name__ == "__main__":
#     N = 10
#     arr = []
#     ln = 1000
#     for i in range(ln):
#         arr.append(random.randint(1, 1000))

#     kis = [0, ln//2, ln-1]
#     bench(main.kthSmallestV8, arr, N, kis)
#     bench(main.kthSmallestV7, arr, N, kis)
#     bench(main.kthSmallestV6, arr, N, kis)
#     bench(main.kthSmallestV5, arr, N, kis)
#     bench(main.kthSmallestV4, arr, N, kis)
#     bench(main.kthSmallestV3, arr, N, kis)
#     bench(main.kthSmallestV2, arr, N, kis)
#     bench(main.kthSmallestV1, arr, N, kis)
#     print("----------------------")




def bench(fn, arr, N, ks):
    try:
        start = time.time()
        for _ in range(N):
            for k in ks:
                res = arr.copy()
                l = 0
                r = len(res) - 1
                fn(arr, l, r, k)
        print(fn.__name__, time.time() - start)
    except Exception as e:
        print(fn.__name__, e)
        # raise e


if __name__ == "__main__":
    N = 1
    arr = []
    ln = 1000
    for i in range(ln):
        arr.append(random.randint(1, 1000))

    ks = [v+1 for v in range(0, ln, 3)]

    bench(main.kthSmallestV8, arr, N, ks)
    bench(main.kthSmallestV7, arr, N, ks)
    bench(main.kthSmallestV6, arr, N, ks)
    bench(main.kthSmallestV5, arr, N, ks)
    bench(main.kthSmallestV4, arr, N, ks)
    bench(main.kthSmallestV3, arr, N, ks)
    bench(main.kthSmallestV2, arr, N, ks)
    bench(main.kthSmallestV1, arr, N, ks)
    print("----------------------")