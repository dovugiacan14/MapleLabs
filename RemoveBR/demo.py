from rembg import remove
import cv2

input_path = 'images/tiger.png'
output_path = 'images/out.png'

input = cv2.imread(input_path)
output = remove(input)
cv2.imwrite(output_path, output)