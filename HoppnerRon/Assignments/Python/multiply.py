def multiply(a,b):
	
	x = []
	for i in range(len(a)):
		y = a[i] * b
		x.append(y)
	print x

multiply([1,2,3,4,5,6,7,8,9,10],10)