def draw_stars([])
	
	count = 0

	for i in range(len(a)):
		count += a[i]
		print '*' * count

draw_stars([1,2,3])


def myfun(x):
for ele in x:
	if type(ele)==(int, long):
		print '*' * ele
	else: 
		print ele[0].lower() * len(ele)