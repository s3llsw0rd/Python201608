from system.core.model import Model
from flask import jsonify

class Lead(Model):
	def __init__(self):
		super(Lead, self).__init__()
	
	def get_leads_between(self, name, early, late, page):
		query = 'SELECT * FROM leads'
		data = {}
		prev = False
		if name != '':
			query += ' WHERE CONCAT(first_name, " ", last_name) LIKE "%":name"%"'
			prev = True
			data['name'] = name
		if early != '':
			if prev:
				query += ' AND'
			else: query += ' WHERE'
			query += ' registered_datetime > :start'
			prev = True
			data['start'] = early
		if late != '':
			if prev:
				query += ' AND'
			else: query += ' WHERE'
			query += ' registered_datetime < :stop'
			data['stop'] = late
		query += ' ORDER BY registered_datetime DESC'
		pages = self.db.query_db(query, data)
		query += ' LIMIT :offset, 10'
		data['offset'] = int(page)*10-10
		results = self.db.query_db(query, data)
		return jsonify({'people': results, 'pages': pages})