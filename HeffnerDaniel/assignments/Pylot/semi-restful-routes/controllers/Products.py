from system.core.controller import *

class Products(Controller):
	def __init__(self, action):
		super(Products, self).__init__(action)
		self.load_model('Product')
		self.db = self._app.db

	def index(self):
		products = self.models['Product'].get_all_products()
		return self.load_view('index.html', products=products)

	def new(self):
		return self.load_view('new.html')

	def edit(self, id):
		product = self.models['Product'].get_one_product(id)
		return self.load_view('edit.html', product=product[0])

	def show(self, id):
		product = self.models['Product'].get_one_product(id)
		return self.load_view('show.html', product=product[0])

	def create(self):
		self.models['Product'].create_product(request.form)
		return redirect('/products')

	def destroy(self, id):
		self.models['Product'].destroy_product(id)
		return redirect('/products')

	def update(self, id):
		self.models['Product'].update_product(request.form)
		return redirect('/products')



"""
A loaded model is accessible through the models attribute 
self.models['WelcomeModel'].get_users()

self.models['WelcomeModel'].add_message()
# messages = self.models['WelcomeModel'].grab_messages()
# user = self.models['WelcomeModel'].get_user()
# to pass information on to a view it's the same as it was with Flask

# return self.load_view('index.html', messages=messages, user=user)
"""