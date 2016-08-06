import time
import random

def timer(func):
    def wrapper(*arg,**kwarg):
        t = 0
        for i in range(iterations):
            start =  time.time()
            func(*arg,**kwarg)
            end  = time.time()
            t+= (end-start)
        print t/iterations*1000
    return wrapper

@timer
def insertionSort(array):
    for i in range(1,len(array)):
        count = 0
        for j in reversed(range(i)):
            if array[i] < array[j]:
                count +=1
        array.insert(i-count,array[i])
        array.pop(i+1)
    print array
    return array

arr = [random.random() for i in range(100)]
iterations = 1

insertionSort(arr)
