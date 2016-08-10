import re

with open('us-500.csv', 'rU') as file:
	h = file.readline()
	in_entry = False
	header = ''
	headers = []
	for c in h:
		if c == '"':
			if in_entry:
				in_entry = False
				headers.append(header)
				header = ''
				continue
			else:
				in_entry = True
				continue
		if in_entry:
			header += c

	read_file = file.read()

	datum = ''
	data = []
	all_data = []
	count = 0
	in_entry = False

	for c in read_file:
		if c == '"':
			if in_entry:
				in_entry = False
				continue
			else:
				in_entry = True
				continue
		if not in_entry and (c == ',' or c =='\n'):
			if datum == '':
				datum = 'n/a'
			data.append(datum)
			datum = ''
			count += 1
			if count == len(headers):
				print data
				all_data.append(data)
				data = []
				count = 0
			continue
		if not in_entry and re.match('[0-9]', c):
			datum+=c
		if in_entry:
			datum += c

	output = []
	for row in all_data:
		output.append({key: ele for key, ele in zip(headers, row)})
	for entry in output:
		print entry['first_name']+' '+entry['last_name']
		print 'first_name: '+entry['first_name']
		print 'last_name: '+entry['last_name']
		print 'company_name: '+entry['company_name']
		print 'address: '+entry['address']
		print 'city: '+entry['city']
		print 'county: '+entry['county']
		print 'state: '+entry['state']
		print 'zip: '+entry['zip']
		print 'phone1: '+entry['phone1']
		print 'phone2: '+entry['phone2']
		print 'email: '+entry['email']
		print 'web: '+entry['web']
		print '--------------------------------'