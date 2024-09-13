#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Video.py
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
import threading
import time
from imutils.video import VideoStream


class Video():
    
    def __init__(self):
        
        self.outputFrame = None
        self.outputLock = threading.Lock()
        self.lastFrame = time.time()
        
        self.stream = VideoStream(src=0).start()
        time.sleep(2)
        
        
    def frame(self):
        start = time.time()
        # print(f"{self.lastFrame} - {start} = {self.lastFrame - start}")
        if start - self.lastFrame > 1:
            _frame = self.stream.read()
            with self.outputLock:
                self.outputFrame = _frame.copy()
                
            self.lastFrame = start
            
        return self.outputFrame
        
    def close(self):
        self.stream.stop()

