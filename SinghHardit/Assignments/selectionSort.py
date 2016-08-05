import random
import time

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
def selectionSort(arr):
    start = 0
    while start < len(arr):
        minVal = arr[start]
        minIndex = 0
        for n,i in enumerate(arr[start:len(arr)]):
            if i < minVal:
                minVal = i
                minIndex = n
        arr[start],arr[minIndex+start] = arr[minIndex+start],arr[start]
        start+=1
    return arr
    #print arr

arr = [random.random() for i in range(100)]
iterations = 100000
#t = 0
#for i in range(iterations):
#    start =  time.time()
#    selectionSort(arr)
#    end = time.time()
#    t+=(end-start)
#print t/iterations*1000

selectionSort(arr)
