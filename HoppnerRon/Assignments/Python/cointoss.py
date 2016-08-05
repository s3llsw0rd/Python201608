import random

heads_count = 0
tails_count = 0
attempt = 1

for i in range (1, 5001):
		flip = random.random()
		if flip > 0.499999999999:
			heads_count += 1
			print 'Attempt #' + str(attempt) + ': Throwing a coin...It\s a head!...Got ' + str(heads_count) + '(s) so far and ' + str(tails_count) + 'tail(s) so far'
			attempt += 1
		elif flip < 0.499999999999:
			tails_count += 1
			print 'Attempt #' + str(attempt) + ': Throwing a coin...It\s a tail!...Got ' + str(heads_count) + '(s) so far and ' + str(tails_count) + 'tail(s) so far'
			attempt += 1





