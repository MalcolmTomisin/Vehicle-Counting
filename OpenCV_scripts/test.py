import cv2
from VideoGet import VideoGetStream
from imutils.video import FPS


def threadVideoGet(source):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Main thread shows video frames.
    """

    video_getter = VideoGetStream(source).start()
    fps = FPS().start()

    while True:
        if (cv2.waitKey(1) == ord("q")) or video_getter.stopped:
            video_getter.stop()
            fps.stop()
            print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
            print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
            break

        frame = video_getter.frame
        cv2.imshow("Video", frame)

        threadVideoGet('../videos/IMG_0396.MOV')
