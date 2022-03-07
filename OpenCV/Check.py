import cv2 # opencv读取的格式是BGR，与matplotlib不同
import matplotlib.pyplot as plt
import numpy as np

vc = cv2.VideoCapture('/Users/xiaoziqi/Desktop/Code/deep-learning/OpenCV/data/test.mp4')

if vc.isOpened():
    is_open, frame = vc.read()
else:
    is_open = False

while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret:
        v_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', v_gray)
        if cv2.waitKey(100) & 0xFF == 27:
            break
vc.release()
cv2.destroyAllWindows()