number = 1

for count in range(1,2001):
	if number % 2 != 0:
		print str(number) + ' is an odd number.'
	elif number % 2 == 0:
		print str(number) + ' is an even number.' 
	number += 1