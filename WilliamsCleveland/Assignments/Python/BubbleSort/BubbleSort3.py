import random
import timeit
import time


def timer(func):
    def sort_bubble(*arg, **kwarg):
        t = 0
        for i in range(iterations):
            start = time.time()
            func(*arg, **kwarg)
            end = time.time()
            t += (end - start)
        print t / iterations * 1000
    return sort_bubble


@timer
def bubble_sort(arr):
    length = len(arr) - 1
    while length > 0:
        for i in range(length):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        length -= 1
    print arr

arr = [random.randint(0, 10000) for i in range(50)]
iterations = 1

bubble_sort(arr)
