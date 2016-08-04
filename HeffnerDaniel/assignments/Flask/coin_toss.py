import random
heads = 0
tails = 0
for i in range(1,5001):
	flip = random.random()
	if round(flip)==0:
		heads += 1
		print "Attempt #"+str(heads+tails)+": Throwing a coin... It's heads! ... Got",str(heads),"head(s) so far and",str(tails),"tail(s) so far"
	elif round(flip)==1:
		tails += 1
		print "Attempt #"+str(heads+tails)+": Throwing a coin... It's tails! ... Got",str(heads),"head(s) so far and",str(tails),"tail(s) so far"
print "Ending the program, thank you!"