import cv2
from imutils.video import FPS
from FileThreadClass import FileVideoStream
import numpy as np
import time

    

fvs = FileVideoStream('../videos/IMG_0396.MOV').start()
time.sleep(1.0)

fps = FPS().start()

while fvs.more():
        if (cv2.waitKey(1) == ord("q")):
            fps.stop()
            print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
            print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
            break

        frame = fvs.read()
        print("[INFO] elasped time")
        frame = np.dstack([frame, frame, frame])
        cv2.putText(frame, "Queue Size: {}".format(fvs.Q.qsize()),
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow("Video", frame)
        fps.update()
     


