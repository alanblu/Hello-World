import cv2

imagen = cv2.imread('ironyo,jpg',cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('foto2.jpg',imagen)
