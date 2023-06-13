#Rendering in real time
import cv2
import recognize
import logging
import attendance
import time
import importlib
import sklearn
import warnings
warnings.filterwarnings("ignore")

logging.basicConfig(filename='realtime.log',level = logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def realtime():
    try:
        cap = cv2.VideoCapture('rtsp://admin:123456@192.168.1.91/H264?ch=8&subtype=0')
        # cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret,frame = cap.read()        
            cv2.imshow('Webcam',frame)
            a,b = recognize.reg_test(frame)
            # if a == None or b==None:
            #     a = ['No Face']
            #     b = ['Detected']
            #print('Im here',ret)
            c = time.time()
            readable_time = time.localtime(c)
            c = time.strftime("%d/%m/%Y %H:%M:%S", readable_time)
            logging.info((a,b))
            # logging.info(b)
            #print(c,a,b)
            #attendance.three(c,a,b)
            # attendance.attendance()
            print(c,a)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        logging.debug(e)
realtime()

