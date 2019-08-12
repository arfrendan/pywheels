import numpy as np
import cv2
import imutils
from pyzbar import pyzbar

cap = cv2.VideoCapture(0)

def decode(image):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        (x,y,w,h) = barcode.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),5)
        
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        
        text = "{}({})".format(barcodeData,barcodeType)
        cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        return barcodeData
        
        
while(True):
    mat,frame = cap.read()
    cv2.imshow("frame",frame)
    if mat == True:
        decode(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
