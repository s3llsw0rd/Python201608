import csv

with open ('us-500.csv', 'rU') as file:
	read = csv.reader(file, dialect=csv.excel)
	headers = read.next()
	output = []
	for row in read:
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

