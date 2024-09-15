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

from flask import Flask
from View.CameraView import CameraView
from View.IndexView import IndexView

import argparse


def main(args):
    app = Flask("CamStream")

    IndexView.register(app)
    CameraView.register(app)

    argsParser = argparse.ArgumentParser()
    argsParser.add_argument("--port", type=int, default=8080, help="port to listen on", required=False)
    argsParser.add_argument("--host", type=str, default="0.0.0.0", help="ip to bind", required=False)
    argsParser.add_argument("--debug", action="store_true", default=False, help="debug mode", required=False)
    args = vars(argsParser.parse_args())

    app.run(host=args["host"], port=args["port"], debug=args["debug"], threaded=True, use_reloader=False, ssl_context='adhoc')

    CameraView.camera.close()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
