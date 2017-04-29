from django.http import HttpResponse
from django.template import loader
import cv2
import numpy as np
import base64
import os

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

def upload(request):
	if request.POST:
		curr_dir = os.path.dirname(__file__)
		face_cascade = cv2.CascadeClassifier(os.path.join(curr_dir, 'haarcascade_frontalface_alt2.xml'))
		eye_cascade = cv2.CascadeClassifier(os.path.join(curr_dir,'haarcascade_eye.xml'))
		if face_cascade.empty(): 
			print('FACE_CASCADE IS NOT LOADING')
		if eye_cascade.empty():
			print('EYE_CASCADE IS NOT LOADING')
		#print(request.POST)
		imgStr = request.POST['img']
		#print('First: ' + imgStr[:100])
		imgStr = imgStr.replace('data:image/jpeg;base64,','')
		imgStr = imgStr.replace(' ', '+')
		#print('Second: ' + imgStr[:100])
		nparr = np.fromstring(base64.b64decode(imgStr), np.uint8)
		#print('Third, nparr: ' + nparr)
		img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		#u'data:image/jpeg;base64,
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
			eyes = eye_cascade.detectMultiScale(roi_gray)
			if len(eyes) == 0:
				return HttpResponse("3") #0 changed to 3
			return HttpResponse("1")
		return HttpResponse("4")
 
	else:	
		return HttpResponse("good try.")
