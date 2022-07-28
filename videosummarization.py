import cv2 # pip install opencv-python
import numpy as np # pip install numpy
from datetime import timedelta
import pprint

video = cv2.VideoCapture('/content/Videosummary_2/1.mp4')
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
threshold = 20.
FPS = 2.0
writer = cv2.VideoWriter('/content/Videosummary_2/fin.mp4', cv2.VideoWriter_fourcc(*'MJPG'), FPS, (width, height))
ret, frame1 = video.read()
prev_frame = frame1

a = 0
b = 0
c = 0
frame_counter = 0
frame_counter_2 = 0
str_op = ""
fin_dct = {}
lst = ["End"]
while True:
    ret, frame = video.read()
    if ret is True:
        if (((np.sum(np.absolute(frame-prev_frame))/np.size(frame)) > threshold)):
            #print(frame)
            writer.write(frame)
            prev_frame = frame
            a += 1
            frame_counter+=1
            td = timedelta(seconds=(frame_counter / FPS))
            #str_op = "Start_time - " + str(td)
            if  lst[-1] == "End":
                fin_dct['Start_time '+str(frame_counter)] = str(td)
                lst.append("Start")

        else:
            prev_frame = frame
            b += 1
            frame_counter+=1
            td2 = timedelta(seconds=(frame_counter / FPS))
            #print("End_Time - "+ str(td2))
            if  lst[-1] == "Start":
                fin_dct['End_Time '+str(frame_counter)] = str(td2)
                lst.append("End")
            #cv2.imshow('frame', frame)
            c += 1
        #print(len(fin_dct))
        if len(fin_dct) > 880:
            video.release()
            writer.release()
            cv2.destroyAllWindows()
            pp = pprint.PrettyPrinter(depth=4)
            pp.pprint(fin_dct)
            #print(fin_dct)
            print("Total frames: ", c)
            print("Unique frames: ", a)
            print("Common frames: ", b)
            break
