from system.core.router import routes

routes['default_controller'] = 'Products'

routes['GET']['/products'] = 'Products#index'
routes['GET']['/products/new'] = 'Products#new'
routes['GET']['/products/edit/<id>'] = 'Products#edit'
routes['GET']['/products/show/<id>'] = 'Products#show'
routes['POST']['/products'] = 'Products#create'
routes['POST']['/products/destroy/<id>'] = 'Products#destroy'
routes['POST']['/products/update/<id>'] = 'Products#update'