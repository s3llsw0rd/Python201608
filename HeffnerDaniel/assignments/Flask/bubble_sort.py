import random
import time

x = []
for i in range(100):
	x.append(int(round(random.random()*10000)))

def timer(func):
	def wrapper(*arg, **kw):
		t1 = time.time()
		res = func(*arg, **kw)
		t2 = time.time()
		print (t2-t1)*1000, "ms"
		return (t2 - t1), res, func.__name__
	return wrapper

@timer
def bubbleSort(x):
	changes = 1
	start = time.time()
	while changes>0:
		changes = 0
		for i in range(0, len(x)-1):
			one = x[i]
			two = x[i+1]
			if one > two:
				x[i], x[i+1] = x[i+1], x[i]
				changes += 1
	end = time.time()
	print end - start
	print x

print "testing"
bubbleSort(x)


#I haven't yet figured out how to use datetime to figure out how long the sorting takes