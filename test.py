from __future__ import print_function
import datetime

class FPS:
    def __init__(self):
        self._start = None
        self_end = None
        self._numFrames = 0
        
    def start(self):
        self._start = datetime.datetime.now()
        return self
    
    def stop(self):
        self._end = datetime.datetime.now()
        
    def update(self):
        self._numFrames += 1
        
    def elapsed(self):
        return (self._end - self._start).total_seconds()
    
    def fps(self):
        return self._numFrames / self.elapsed()
    
    
from threading import Thread
import cv2

class camVideoStream:
    def __init__(self,src= 0):
        self.stream = cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        (self.grabbed,self.frame) = self.stream.read()
        
        self.stopped = False
        
    def start(self):
        Thread(target = self.update,args=()).start()
        return self
    
    def update(self):
        while True:
            if self.stopped:
                return
            (self.grabbed,self.frame) = self.stream.read()
            
    def read(self):
        return self.frame
    
    def stop(self):
        self.stopped = True
        

import argparse
import imutils

print("[INFO] sampling frame from cam")
stream = cv2.VideoCapture(0)
stream.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
stream.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
fps = FPS().start()

while fps._numFrames <100:
    (grabbed,frame) = stream.read()
    #frame - imutils.resize(frame,width=400)
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1) & 0xFF
    fps.update()
    
fps.stop()
print("[INFO] elapse time :{:.2f}".format(fps.elapsed()))
print("[INFO] approx fps :{:.2f}".format(fps.fps()))

stream.release()
cv2.destroyAllWindows()


print("[INFO] sampling threaded frames from cam")
vs = camVideoStream(src = 0).start()
fps = FPS().start()

while fps._numFrames <100:
    frame = vs.read()
    cv2.imshow("frame2",frame)
    key = cv2.waitKey(1) & 0xFF
    fps.update()
    
fps.stop()
print("[INFO] elasped time:{:.2f}".format(fps.elapsed()))
print("[INFO] approx fps :{:.2f}".format(fps.fps()))
cv2.destroyAllWindows()
vs.stop()

