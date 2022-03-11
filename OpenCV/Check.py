import cv2  # opencv读取的格式是BGR，与matplotlib不同
import matplotlib.pyplot as plt
import numpy as np

pic_path = '/Users/xiaoziqi/Desktop/Code/deep-learning/OpenCV/data/cat1.jpeg'
img = cv2.imread(pic_path)


def cv_show(name_image, image):
    # 图像的显示，也可以创建多个窗口
    cv2.imshow(name_image, image)
    # 等待时间，毫秒级，0表示任意键终止
    cv2.waitKey(500)
    cv2.destroyAllWindows()


cur_img = img.copy()
cur_img[:, :, 0] = 0
cur_img[:, :, 1] = 0
cv_show('cur_img', cur_img)
