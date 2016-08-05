def draw_stars(lst):
	for ele in lst: #this will simply iterate over the list. convention dictates the use of "ele".
		if type(ele) == int:
			stars = ""
			for s in range(ele):
				stars += "*"
			print stars
		elif type(ele) == str:
			stars=""
			letter = ele[:1]
			for s in range(len(ele)):
				stars += letter.lower()
			print stars

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
