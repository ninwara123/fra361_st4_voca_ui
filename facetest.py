# import numpy as np
# import cv2
# import os
# cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(cascPath)
# cap = cv2.VideoCapture(0)
# while (True):
#     ret,frame = cap.read()
#     # gray = cv2.imread(frame, cv2.IMREAD_GRAYSCALE)
#     faces = faceCascade.detectMultiScale(
#         frame,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )
#     # Draw a rectangle around the faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     # Display the resulting frame
#     cv2.imshow('Video', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# import numpy as np
# import cv2
# import os
# faceCascade = cv2.CascadeClassifier("D:/IU64/haarcascade_frontalface_default.xml")
# img_id = 0
# def create_dataset(img,id,img_id):
#     cv2.imwrite("data/pic"+str(id)+"."+str(img_id)+".jpg",img)
#     # pass                                   

# def draw_bounddary (img,classifier,scaleFactor,minNeigbors,color,text):
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     features = classifier.detectMultiScale(gray,scaleFactor,minNeigbors)
#     coords = []
#     for (x,y,w,h) in features:
#         cv2.rectangle(img, (x,y), (x+w,y+h),color,2)
#         # cv2.putText(img,text,cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1)
#     return img,coords

# # def detect(img,facecCascade,img_id):
# #     img = draw_bounddary(img,faceCascade,1.1,10,(255,0,0),"face")
# #     print(img)
# #     id = 1
    
#     # cv2.imshow('frame',img)
#     # create_dataset(img,id,img_id)
#     # return img

# n=1
# x = 0
# # frame = cv2.imread("tae1.jpg")
# cap = cv2.VideoCapture(0)

# # scale_percent = 20 # percent of original size
# # width = int(ret.shape[1] * scale_percent / 100)
# # height = int(ret.shape[0] * scale_percent / 100)
# # dim = (width, height)
  
# # # # resize image
# # ret = cv2.resize(ret, dim, interpolation = cv2.INTER_AREA)
# while (True):
#     # ret,frame = frame.read()
#     ret,frame = cap.read()
#     # faces = faceCascade.detectMultiScale(
#     #     frame,
#     #     scaleFactor=1.1,
#     #     minNeighbors=5,
#     #     minSize=(30, 30),
#     #     flags=cv2.CASCADE_SCALE_IMAGE
#     # )
#     # Draw a rectangle around the faces
#     # for (x, y, w, h) in faces:
#     #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     # ret,frame = cap.read()
#     # frame = detect(frame,faceCascade,img_id)
#     # x = x+1
#     # if x%5 == 0:
#     #     cv2.imwrite("data/pic"+str(x)+".jpg",frame)
#     cv2.imshow('frame',frame)
#     if (cv2.waitKey(1) & 0xFF == ord('q')):
#         break
#     n=2
#     # cv2.waitKey(5)
# cap.release()
# cv2.destroyAllWindows()

import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier("D:/IU64/haarcascade_frontalface_default.xml")
# scale_percent = 20 # percent of original size
# width = int(ret.shape[1] * scale_percent / 100)
# height = int(ret.shape[0] * scale_percent / 100)
# dim = (width, height)
  
# # resize image
# ret = cv2.resize(ret, dim, interpolation = cv2.INTER_AREA)
# ret = cv2.resize(ret,)

state = "w"
ttt = "no"
x = "w"
cap = cv2.VideoCapture(0)
def cappic():
    # x = "w"
    ret,frame = cap.read()
    cv2.imshow('video',frame) 
    if(cv2.waitKey(1) & 0xFF == ord("c")):
        if ret:
            cv2.imwrite("data/pic.jpg",frame) 
        # x = "a"
        cv2.destroyAllWindows()       
    # return x
while (True):
    if state == "w":
        state = "cap"
        x = "cap"
    elif state == "a":
        print(state)
        print("aaaaa")
    elif state == x:
        # print(x)
        cappic()
        # cap.release()
        
    # elif state == "crop_pic":
    #     pic = cv2.imread("D:/IU64/data/pic.jpg")
    #     faces = faceCascade.detectMultiScale(
    #         frame,
    #         scaleFactor=1.1,
    #         minNeighbors=5,
    #         minSize=(30, 30),
    #         flags=cv2.CASCADE_SCALE_IMAGE
    #     )
    #     for (x, y, w, h) in faces:
    #         # cv2.rectangle(frame, (x-40, y-90), (x+w+40, y+h+45), (0, 255, 0), 2)
    #         cv2.imwrite("data/croppic.jpg",pic[x-40:x+w+40,y-90:y+h+45]) 
    #     state = "cap"
    #     cv2.destroyAllWindows()
