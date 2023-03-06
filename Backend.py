import cv2
from datetime import datetime
import winsound                    
from Calling import calling  #Local
from Whatsapp import whatsapp #Local

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
sv = '{}.avi'.format(datetime.now().strftime("%d-%m-%Y %H-%M-%S"))
out = cv2.VideoWriter(sv, fourcc,20.0,(640,480))   


def backend():
    t = False
    i = 1
    while True:
        _, frame1 = cap.read()
        _, frame2 = cap.read()
        _, frame3 = cap.read()
        
        # difference between both motions frame1 and frame2
        diff = cv2.absdiff(frame1, frame2)
        # Converting the diff cover into gray
        gray =  cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        # convert gray to blur
        blur  = cv2.GaussianBlur(gray, (5 , 5), cv2.BORDER_DEFAULT)     # (height, width) = (5,5)
        # threshold  the blur into BINARY
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        # Dilation of image it is opposite of threshold it is the actual thing what we require
        dilate = cv2.dilate(thresh, None, iterations=3)
        # contours to find the what is static in image and  dynamic
        contours,_ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if cv2.waitKey(1) == ord('n'):
            t = True
            
        if cv2.waitKey(1) == ord('a'):
            t = False

        for c in contours :
               if cv2.contourArea(c) < 5000 :                                                                                                                                                                                                                      
                   continue
               if t == False :
                   x, y, w, h = cv2.boundingRect(c)
                   vik = cv2.rectangle(frame3, (x,y), (x+w, y+h), (255, 0, 0), 2)
                   cv2.putText(frame3, 'ALLOWED', (25,25), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255), 2)
                
               elif t == True :   
                    x, y, w, h = cv2.boundingRect(c)
                    vik = cv2.rectangle(frame3, (x,y), (x+w, y+h), (0, 0, 255), 2)
                    cv2.putText(frame3, 'NOT ALLOWED', (25,25), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255), 2)
                    winsound.Beep(500, 200)    # (how louder,  how long)
                    whatsapp(i)
                    calling(i)
                    i=i+1
                     
        cv2.putText(frame3, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255), 2)
        cv2.imshow(" Enter q For Exit", frame3)
        out.write(frame3)

            
        if cv2.waitKey(1) == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
      
