from system.core.controller import *

class APIcontrol(Controller):
    def __init__(self, action):
        super(APIcontrol, self).__init__(action)
    def get_directions(self):
        start_loc = request.form['start_loc'].replace(' ','')
        end_loc = request.form['end_loc'].replace(' ','')
        url = 'https://maps.googleapis.com/maps/api/directions/json?origin=' + start_loc + '&destination=' + end_loc + '4&key=AIzaSyBabf4hOCJTux7dIUwkAJNUHZm-9hhWTfY'
        response = requests.get(url).content
        return response

