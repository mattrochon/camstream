from flask_classful import FlaskView
from flask import Response
from Video import Video as video

import time
import cv2


class CameraView(FlaskView):
    camera = video.Video()

    def index(self):
        return Response(self.generate(), mimetype="multipart/x-mixed-replace; boundary=frame")

    def generate(self):
        while True:
            time.sleep(0.05)
            frame = CameraView.camera.frame()
            if frame is None:
                continue
            # encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", frame)
            # ensure the frame was successfully encoded
            if not flag:
                continue
            # yield the output frame in the byte format
            yield b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n'
