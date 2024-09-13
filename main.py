#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2024  <user@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import cv2
import time
from Video import Video as video
from flask import Response
from flask import Flask
from flask import render_template
from flask_classful import FlaskView

app = Flask("CamStream")


class CameraView(FlaskView):
    camera = video.Video()
    
    def index(self):
        return Response(self.generate(), mimetype = "multipart/x-mixed-replace; boundary=frame")

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
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')


CameraView.register(app)
    
@app.route("/")
def index():
    return render_template("./index.html")
    

def main(args):
    app.run(host="0.0.0.0", port="8080", debug=True, threaded=True, use_reloader=False)
    CameraView.camera.close()


if __name__ == '__main__':
    import sys 
    sys.exit(main(sys.argv))
