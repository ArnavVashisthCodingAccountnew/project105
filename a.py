import os
import cv2

path = "Images/"
Images = []

for filename in os.listdir(path):
    name,ext = os.path.splitext(filename)
    if ext in ['.jpg', '.png','.gif','.jpeg','.jfif']:
        file_name = path+"/"+filename
        print(file_name)
        Images.append(file_name)

count = len(Images)
frame = cv2.imread(Images[0])
height,width,layers = frame.shape
size = (width,height)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8, size)
for i in range(0,count-1):
    frame = cv2.imread(Images[i])
    out.write(frame)
    print("Done")
    
#out.release()
