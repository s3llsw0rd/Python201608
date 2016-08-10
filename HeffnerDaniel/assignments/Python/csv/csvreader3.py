import re

with open('Sacramentorealestatetransactions.csv', 'rU') as file:
	h = file.readline()

	header = ''
	headers = []

	for c in h:
		if c == '"':
			continue
		if (c == ',' or c =='\n'):
			if header == '':
				header = 'n/a'
			headers.append(header)
			header = ''
			continue
		header += c

	print headers

	read_file = file.read()

	datum = ''
	data = []
	all_data = []
	count = 0

	for c in read_file:
		if (c == ',' or c =='\n'):
			if datum == '':
				datum = 'n/a'
			data.append(datum)
			datum = ''
			count += 1
			if count == len(headers):
				all_data.append(data)
				data = []
				count = 0
			continue
		datum += c

	output = []
	for row in all_data:
		output.append({key: ele for key, ele in zip(headers, row)})
	for entry in output:
		for key, value in entry.iteritems():
			print key+': '+value
		print '--------------------------------'
