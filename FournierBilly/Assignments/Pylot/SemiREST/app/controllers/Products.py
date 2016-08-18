"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('ProductModel')
        self.db = self._app.db

    def index(self):
        products = self.models['ProductModel'].get_products()
        return self.load_view('index.html', products=products)

    def new(self):
        return self.load_view('new.html')

    def show(self,id):
        print 'id is: ', id
        products = self.models['ProductModel'].get_product(id)
        print products
        return self.load_view('show.html', products=products)

    def edit(self,id):
        product = self.models['ProductModel'].get_product(id)
        return self.load_view('edit.html', product = product)

    def create(self):
        product_info = request.args
        errors = self.models['ProductModel'].create_product(product_info)
        if errors:
            for ele in errors:
                flash(ele)
        return redirect('/')

    def delete(self,id):
        self.models['ProductModel'].delete_product(id)
        return redirect('/')

    def update(self,id):
        updated_info = request.form
        self.models['ProductModel'].update_product(id,updated_info)
        return redirect('/products/show/'+id)
