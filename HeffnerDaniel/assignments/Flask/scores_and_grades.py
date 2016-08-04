def score_grade():
	score = raw_input()
	score = int(score)
	if score >= 60 and score < 70:
		print "Score: "+str(score)+"; Your grade is D"
	elif score >= 70 and score < 80:
		print "Score: "+str(score)+"; Your grade is C"
	elif score >= 80 and score < 90:
		print "Score: "+str(score)+"; Your grade is B"
	elif score >= 90 and score <= 100:
		print "Score: "+str(score)+"; Your grade is A"
	else:
		print "error, illegal score"

print "Scores and Grades"
for i in range(0,10):
	print "Please enter a score between 60 and 100:"
	score_grade()
print "End of the program. Bye!"