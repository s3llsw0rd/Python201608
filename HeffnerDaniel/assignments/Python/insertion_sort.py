import random
import time

'''
PSEUDO CODE
Note: I made attempts at pseudo code for the other sorting algorithms, but this is
the first time that I've really fleshed it out. There appear to be a number of 
standards for pseudo code out there, so I'd appreciate some feedback/advice about
this pseudo code. I'm trying to stick pretty close to the guidelines in the 
learning platform.

set arr to be an array of integers
set i to be 0
if i is equal to the length of arr, go to line 25
	set temp to be the value of arr at i
	set j to be i - 1
		if j is less than 0 go to line 22
		if the value of arr at j is less than temp then go to line 22
			set value of arr at j+1 to be the value of arr at j
			decrement j
			go to line 17
	set the value of arr at j+1 to be temp
	increment i
	go to line 14
END
'''

x = []
for i in range(100):
	x.append(random.randint(0,10000))

def insertSort(lst):
	for i in range(len(lst)):
		t1 = time.clock()
		temp = lst[i]
		j = i - 1
		while j >= 0 and lst[j] >= temp:
			lst[j+1] = lst[j]
			j -= 1
		lst[j+1] = temp
	t2 = time.clock()
	print str((t2-t1)*1000000)+" microseconds"
	return lst

print insertSort(x)
