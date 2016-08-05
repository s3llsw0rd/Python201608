#Coin toss!!!

import random

flips = 0
heads = 0
tails = 0
while flips < 5000:
	headsortails = random.randint(1,2)
	
	if heads or tails == 1:
		heads = heads + 1

	if headsortails == 2:
		tails = tails + 1

	flips = flips + 1

print('Its  heads you got ' + str(heads),  'so far and ' + str(tails), 'tails so far ')
print('Its tails you got ' + str(tails),  'so far and ' + str(heads), 'heads so far ')
print('You flipped ' + str(flips), 'times')

