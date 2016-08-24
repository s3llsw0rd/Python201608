from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
	now = datetime.datetime.now()
	context = {
		'date': now.strftime('%b %d, %Y'),
		'time': now.strftime('%I:%M:%S %p')
	}
	return render(request, 'timedisplay/index.html', context)