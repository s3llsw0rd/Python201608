from system.core.router import routes

routes['default_controller'] = 'Welcome'

# View Handlers
routes['GET']['/signin'] = 'Users#signin'
routes['GET']['/register'] = 'Users#register'
routes['GET']['/dashboard'] = 'Users#dashboard'
routes['GET']['/users/edit'] = 'Users#edit'
routes['GET']['/users/show/<id>'] = 'Users#show'
routes['GET']['/logoff'] = 'Users#logoff'
# Model Interactions
routes['POST']['/users/create'] = 'Users#create'
routes['POST']['/users/login'] = 'Users#login'
routes['POST']['/users/edit/update'] = 'Users#update'

# View handlers
routes['GET']['/dashboard/admin'] = 'Admins#admin'
routes['GET']['/users/new'] = 'Admins#new'
routes['GET']['/users/edit/<id>'] = 'Admins#edit'
# Model Interactions
routes['GET']['/admin/destroy/<id>'] = 'Admins#destroy'
routes['POST']['/admin/update/<id>'] = 'Admins#update'
routes['POST']['/users/create'] = 'Users#create'

# Messages Model Interactions
routes['POST']['/messages/create/<id>'] = 'Messages#create'
routes['POST']['/messages/comment/<id>'] = 'Messages#comment'