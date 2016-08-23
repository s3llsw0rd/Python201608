from system.core.controller import *

class Leads(Controller):
    def __init__(self, action):
        super(Leads, self).__init__(action)
        self.load_model('Lead')
   
    def index(self):
        return self.load_view('index.html')

    def get_leads(self):
        early = request.form['from']
        late = request.form['to']
        name = request.form['name']
        page = request.form['page']
        leads = self.models['Lead'].get_leads_between(name, early, late, page)
        return leads

