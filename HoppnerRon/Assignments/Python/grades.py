def grades():
	count = 1

	print "Please enter the score"
	while count <= 10:

		x = int(raw_input())
	
		if x < 60:
			print "Grade out of range."
		elif x > 100:
			print "Grade out of range."
		elif x >= 60 and x <= 69: 
			print 'Your grade is D'
		elif x >= 70 and x <= 79: 
			print 'Your grade is C'
		elif x >= 80 and x <= 89: 
			print 'Your grade is B'
		elif x >= 90 and x <= 100: 
			print 'Your grade is A'
	count += 1
	

grades()
