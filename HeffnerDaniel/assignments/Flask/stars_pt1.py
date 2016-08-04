def draw_stars(lst):
	for ele in lst: #this will simply iterate over the list. convention dictates the use of "ele".
		stars = ""
		for s in range(ele):
			stars += "*"
		print stars

x = [4,6,1,3,5,7,25]
draw_stars(x)