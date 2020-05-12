import cv2
import numpy as np
import matplotlib.pyplot as plt


def crop(frame,left,top,w,h):
    return frame[top:top+h,left:left+w]



def main():
    
    w = 800
    h = 600
    
    left=0
    top=300
    height=250
    width=800
    font = cv2.FONT_HERSHEY_SIMPLEX

    cap = cv2.VideoCapture(0)
    
    cap.set(3, w)
    cap.set(4, h)
    
#    print(cap.get(3))
#    print(cap.get(4))
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    cars=0.0
    
    while ret:
        cars+=0.01
        txt_title1="Cars counter : "+str(int(cars))
        d = cv2.absdiff(frame1, frame2)
        grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey, (5, 5), 0)
        ret, th = cv2.threshold( blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(th, np.ones((3, 3), np.uint8), iterations=1 )
        #eroded = cv2.erode(blur, np.ones((3, 3), np.uint8), iterations=1 )
        eroded = cv2.erode(dilated, np.ones((3, 3), np.uint8), iterations=1 )
        c, h = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame1, c, -1, (0, 25, 230), 2)


        eroded=crop(eroded,left,top,width,height)
        eroded=cv2.GaussianBlur(eroded, (25, 25), 0)
        frame1 = cv2.rectangle(frame1,(0,0),(800,10),(100,10,120),100)

        cv2.putText(frame1,txt_title1,(10,50), font, 1,(255,255,255),2,cv2.LINE_AA)

        cv2.imshow("Work",eroded)
        cv2.imshow("input", frame1)
        #plt.imshow(frame1,cmap='gray')
        if cv2.waitKey(1) == 27: # exit on ESC
            break
        
        frame1 = frame2
        ret, frame2 = cap.read()

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()