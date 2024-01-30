"""
Tuấn Anh, nt.anh.fai@gmail.com
Create Date: $
Create Time: $
"""
import os
import cv2


class Camera:
    def __init__(self):
        pass
    
    def openCamera(self):
        self.vid = cv2.VideoCapture(0)
        self.cnt = 0
    
    def closeCamera(self):
        self.vid.release()
    
    def get(self):
        # Chụp từng khung hình video
        ret, frame = self.vid.read()
        return ret, frame


if __name__ == '__main__':
    pass
