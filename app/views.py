from django.http import HttpResponse
from django.template import loader
import cv2
import numpy as np

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
	    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  

        img = cv2.imread(image) 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            if len(eyes) == 0:
                return 0
            return 1
 
	else:	
		return HttpResponse("good try.")
