def multiply(lst,num):
	for idx in range(len(lst)):
		lst[idx] *= num
	return lst

a = [2,4,10,16]
b = multiply(a,5)
print b