import dlib
import cv2
import os
import numpy as np
import time
"""
Important Note: to convert into video feed We need to make some loop changes. 
"""
img_name = '\\face2.jpg'
img_path = os.getcwd()+'\\Images'+img_name 

frame = cv2.imread(img_path)
frame = cv2.resize(frame,(400,400))
# cap = cap.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
entered=0


def Detect_face_landmarks(frame,detector,predictor,entered,img_path):
	while True:
		np_arr = np.empty(0)
		c = cv2.waitKey(1)
		# if c == ord('a'):
		# 	print('hello')
		if c == 27:
			return 'exited'

		# ret,frame = cap.read()
		grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)	
		lines=[]
		faces = detector(grayImg)
		if entered == 0:
			for face in faces:
				x1 = face.left()
				y1 = face.top()
				x2 = face.right()
				y2 = face.bottom()
				print('face')
				entered=1
				break


			# landmarks = predictor(grayImg,face)

		if c == ord('1'):
			lines=[]
			frame = cv2.imread(img_path)#read, resize and convert to gray scale to remove previous effects
			frame = cv2.resize(frame,(400,400))
			grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			landmarks = predictor(grayImg,face)
			for i in range(0,17):#jaw
				x = landmarks.part(i).x
				y = landmarks.part(i).y			
				cv2.circle(frame,(x,y),1,(255,0,0),-1)
				lines.append((x,y))
			n=0	
			while n+1!=len(lines):
				start_point = lines[n]
				end_point = lines[n+1]
				cv2.line(frame,start_point,end_point,(255,0,0),1)
				n+=1
				
			lines=[]	

				
			
		if c == ord('2'):#right eyebrow

			frame = cv2.imread(img_path)
			frame = cv2.resize(frame,(400,400))
			grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			landmarks = predictor(grayImg,face)
			for i in range(18,22): #right eyebrow
				x = landmarks.part(i).x
				y = landmarks.part(i).y			
				cv2.circle(frame,(x,y),1,(255,0,0),-1)
				lines.append((x,y))

			n=0	
			while n+1!=len(lines):
				start_point = lines[n]
				end_point = lines[n+1]
				cv2.line(frame,start_point,end_point,(255,0,0),1)
				n+=1
			lines=[]	

		if c == ord('3'):#left eye brow
			frame = cv2.imread(img_path)
			frame = cv2.resize(frame,(400,400))
			grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			landmarks = predictor(grayImg,face)
			for i in range(22,27): #left eye brow
				x = landmarks.part(i).x
				y = landmarks.part(i).y			
				cv2.circle(frame,(x,y),1,(255,0,0),-1)
				lines.append((x,y))

			n=0	
			while n+1!=len(lines):
				start_point = lines[n]
				end_point = lines[n+1]
				cv2.line(frame,start_point,end_point,(255,0,0),1)
				n+=1
			lines=[]	
		
		if c == ord('4'):#nose
			frame = cv2.imread(img_path)
			frame = cv2.resize(frame,(400,400))
			grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			landmarks = predictor(grayImg,face)
			for i in range(27,36): #nose
				x = landmarks.part(i).x
				y = landmarks.part(i).y			
				cv2.circle(frame,(x,y),1,(255,0,0),-1)
				# lines.append((x,y))

			# n=0	
			# while n+1!=len(lines):
			# 	start_point = lines[n]
			# 	end_point = lines[n+1]
			# 	cv2.line(frame,start_point,end_point,(255,0,0),1)
			# 	lines.append((x,y))
			# 	n+=1
			# lines=[]	

		if c == ord('5'):#right eye
			frame = cv2.imread(img_path)
			frame = cv2.resize(frame,(400,400))
			grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			landmarks = predictor(grayImg,face)
			for i in range(36,42): #right eye
				x = landmarks.part(i).x
				y = landmarks.part(i).y			
				cv2.circle(frame,(x,y),1,(255,0,0),-1)
				lines.append((x,y))

			n=0	
			while n+1!=len(lines):
				start_point = lines[n]
				end_point = lines[n+1]
				cv2.line(frame,start_point,end_point,(255,0,0),1)
				n+=1
			lines=[]	
				
		if c == ord('6'):#left eye
			frame = cv2.imread(img_path)
			frame = cv2.resize(frame,(400,400))
			grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			landmarks = predictor(grayImg,face)
			for i in range(42,48): #left eye
				x = landmarks.part(i).x
				y = landmarks.part(i).y			
				cv2.circle(frame,(x,y),1,(255,0,0),-1)	
				lines.append((x,y))	

			n=0	
			while n+1!=len(lines):
				start_point = lines[n]
				end_point = lines[n+1]
				cv2.line(frame,start_point,end_point,(255,0,0),1)
				n+=1
			lines=[]							
		# cv2.resizeWindow('Detection window', 400,400)	
		# cv2.imshow('Detection window', frame)

		if c == ord('7'):#upper lip
			frame = cv2.imread(img_path)
			frame = cv2.resize(frame,(400,400))
			grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			landmarks = predictor(grayImg,face)
			for i in range(48,55): #upper lip
				x = landmarks.part(i).x
				y = landmarks.part(i).y			
				cv2.circle(frame,(x,y),1,(255,0,0),-1)		
				lines.append((x,y))

			n=0	
			while n+1!=len(lines):
				start_point = lines[n]
				end_point = lines[n+1]
				cv2.line(frame,start_point,end_point,(255,0,0),1)
				n+=1
			lines=[]
										
		# cv2.resizeWindow('Detection window', 400,400)	
		# cv2.imshow('Detection window', frame)

		if c == ord('8'):#lower lip
			frame = cv2.imread(img_path)
			frame = cv2.resize(frame,(400,400))
			grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			landmarks = predictor(grayImg,face)
			for i in range(55,60): #lower lip
				x = landmarks.part(i).x
				y = landmarks.part(i).y			
				cv2.circle(frame,(x,y),1,(255,0,0),-1)
				lines.append((x,y))

			n=0	
			while n+1!=len(lines):
				start_point = lines[n]
				end_point = lines[n+1]
				cv2.line(frame,start_point,end_point,(255,0,0),1)
				n+=1
			lines=[]	

		# cv2.resizeWindow('Detection window', 400,400)	
		# cv2.imshow('Detection window', frame)

		if c == ord('9'):#inner lips
			frame = cv2.imread(img_path)
			frame = cv2.resize(frame,(400,400))
			grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			landmarks = predictor(grayImg,face)
			for i in range(61,68): #inner lips
				x = landmarks.part(i).x
				y = landmarks.part(i).y			
				cv2.circle(frame,(x,y),1,(255,0,0),-1)		
				lines.append((x,y))

			n=0	
			while n+1!=len(lines):
				start_point = lines[n]
				end_point = lines[n+1]
				cv2.line(frame,start_point,end_point,(255,0,0),1)
				n+=1
			lines=[]		

		if c == ord('0'):#lips
			poly_list=[]
			frame = cv2.imread(img_path)
			frame = cv2.resize(frame,(400,400))
			grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			landmarks = predictor(grayImg,face)
			for i in range(48,60): #lips
				x = landmarks.part(i).x
				y = landmarks.part(i).y			
				# cv2.circle(frame,(x,y),1,(255,0,0),-1)		
				lines.append((x,y))


			# n=0	
			# while n+1!=len(lines):
			# 	start_point = lines[n]
			# 	end_point = lines[n+1]
			# 	cv2.line(frame,start_point,end_point,(255,0,0),1)
			# 	n+=1

			# cv2.line(frame,lines[0],lines[-1],(255,0,0),1)	
			for each_point in lines:
				poly_list.append(list(each_point)) 
			lines=[]		
			pts = [poly_list] # keep polylist in another list
			# print('polylist')
			# print(pts)
			pts = np.array(pts,np.int32)					
			# print(pts)
			# print("+++++++++++++++++++++++++++++")
			# pts = pts.reshape((-1,1,2))
			print('color')
			# cv2.fillPoly(frame,pts,(0,0,255))	
			# time.sleep(3)
			# print('sleep done')
			# cv2.fillPoly(frame,pts,(0,255,255))	
			# time.sleep(3)
			# print('sleep done')
			# cv2.fillPoly(frame,pts,(255,0,255))	
			# time.sleep(3)
			# print('sleep done')
			# cv2.fillPoly(frame,pts,(55,126,100))	
			# time.sleep(3)
			# print('sleep done')
			# cv2.fillPoly(frame,pts,(0,0,0))	
			# time.sleep(3)
			# print('sleep done')
			cv2.fillPoly(frame,pts,(91,52,255))	
			

		# cv2.resizeWindow('Detection window', 400,400)	
		# cv2.imshow('Detection window', frame)

		# if c == ord('0'):#left eye
		# 	frame = cv2.imread(img_path)
		# 	frame = cv2.resize(frame,(400,400))
		# 	grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		# 	landmarks = predictor(grayImg,face)
		# 	for i in range(43,48): #left eye
		# 		x = landmarks.part(i).x
		# 		y = landmarks.part(i).y			
		# 		cv2.circle(frame,(x,y),1,(255,255,0),-1)								
		cv2.resizeWindow('Detection window', 400,400)	
		cv2.imshow('Detection window', frame)

		# c = cv2.waitKey(1)
		# if c == ord('a'):
		# 	print('hello')
		# if c == 27:
		# 	return 'exited'

status = Detect_face_landmarks(frame,detector,predictor,entered,img_path)

# cap.release()
cv2.destroyAllWindows()