from django.http import HttpResponse
from django.template import loader
import cv2

def index(request):
	#template = loader.get_template('app/index.html')
	#return HttpResponse("<h1>Hello world!</h1>")
	
	template = loader.get_template('app/index.html')
	
	context = {
		'none': None,
	}
	return HttpResponse(template.render(context, request))
	
	#return HttpResponse(template.render(request))

def test(request):
	template = loader.get_template('app/test.html')
	return HttpResponse(template.render(None, request))

def upload(request, image):
	if request.POST:

	else:	
		return HttpResponse("good try.")