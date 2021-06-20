from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime


def getScreenMetrics():
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    return width, height


def getTimeStamp():
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    return time_stamp


def fileFormat(time_stamp, width, height):
    file_name = f"{time_stamp}.mp4"
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    caputred_video = cv2.VideoWriter(file_name, fourcc, 50.0, (width, height))
    webcam = cv2.VideoCapture(0)
    return caputred_video, webcam


def main():
    width, height = getScreenMetrics()
    time_stamp = getTimeStamp()

    caputred_video, webcam = fileFormat(time_stamp, width, height)

    while True:
        # Capture the image from the screen
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        # read the image as a numpy array
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        _, frame = webcam.read()
        resize = cv2.resize(frame, (400, 400))
        resize = cv2.flip(resize, 1)
        fr_height, fr_width, _ = resize.shape
        print(fr_height, fr_width)
        img_final[0:fr_height, 0:fr_width, :] = resize[0:fr_height, 0:fr_width, :]
        cv2.imshow('Secret Capture: Press "Q" to close the program', img_final)
        # cv2.imshow('webcam',frame)
        caputred_video.write(img_final)
        if cv2.waitKey(10) == ord("q"):
            break
        else:
            pass


if __name__ == "__main__":
    main()
