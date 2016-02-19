#Libreria para ocuparse de los colores de calculos map
import numpy as np
#para usar las funciones de delay
import time
#Libreria de openCV
import cv2

#Se declara los limites de los colores de un azul mas intenso a uno menos
blueLower = np.array([100, 67, 0], dtype = "uint8")
blueUpper = np.array([255, 128, 50], dtype = "uint8")


#Se llama a la camara, por defecto la camara en 0 es la del ordenador
camera = cv2.VideoCapture(0)#args["video"])

#El while siempre es verdadero hasta que se manda el comando break
while True:
#se lee la camara, y se obtiene el grabbed (una variable booleana que indica si se pudo obtener un frame de la camara o no) y el frame de la misma (frame una imagen en el tiempo)
	(grabbed, frame) = camera.read()
#Si no fue exitosa la camptura del frame, se sale del while con el break
	if not grabbed:
		break

#cambio de direccion la imagen
	frame = cv2.flip(frame, 1)
#creo una nueva imagen y atenuo los colores que no corresponden al rando de azules
	blue = cv2.inRange(frame, blueLower, blueUpper)
#Optimiza la imagen
	blue = cv2.GaussianBlur(blue, (3, 3), 0)

#Encuentra el contorno de la imagen crada anteriormente
	(cnts, _) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#Pregunta si el contorno es distinto de 0
	if len(cnts) > 0:
#Cuenta el area de los contornos
		cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
#Crea las cordenadas de un rectangulo en los contornos
		rect = np.int32(cv2.cv.BoxPoints(cv2.minAreaRect(cnt)))
		#print rect
#Pinta el rectangulo en la imagen frame
		cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)
#Muestra la imagen frame y blue
	cv2.imshow("Tracking", frame)
	cv2.imshow("Binary", blue)

#Hace un delay de la imagen
	time.sleep(0.025)
#Espera a que se aprete la tecla q 
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
#suelta la camare
camera.release()
#destruye tosas las ventanas
cv2.destroyAllWindows()
