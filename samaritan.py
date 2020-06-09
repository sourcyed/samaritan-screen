import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((720,1280,3), dtype=np.int16)

cv2.line(img, (300,375), (900,375), (255,255,255), 5)

vertices = np.array([ [600,415], [575,460], [625,460] ], np.int32)
pts = vertices.reshape((-1,1,2))
cv2.fillPoly(img, [pts], (0,0,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text="ELIMINATE", org=(300,350), fontFace=font, fontScale=4, color=(255,255,255), thickness=7, lineType=cv2.LINE_AA)

cv2.imwrite("samaritan.jpg", img)
