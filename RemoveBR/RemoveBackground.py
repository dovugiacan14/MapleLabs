import cv2 
import numpy as np 

image = cv2.imread('00009.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

contours, _  = cv2.findContours(thresold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

largest_contour = max(contours, key= cv2.contourArea)

result =np.ones_like(image) * 255 

cv2.drawContours(result, [largest_contour], -1, (0,0,0), -1)

final_result = cv2.bitwise_and(image, result)

cv2.imwrite('result.png', final_result)