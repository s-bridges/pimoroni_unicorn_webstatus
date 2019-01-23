#! usr/bin/env python3

# Seth Bridges - https://github.com/s-bridges

from urllib.request import Request, urlopen
from urllib.error import  URLError
import socket
import os
import unicornhathd as unicorn
import time, colorsys
import numpy

unicorn.brightness(1)

unicorn.rotation(180)

req = Request('https:/magicdb.us')
# you can set the timeout to be less, but if its too quick you may just recieve an error
timeout = 25
socket.setdefaulttimeout(timeout)

status_success = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0],
                [0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,0],
                [0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0],
                [0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
                [0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0],
                [0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

status_fail = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0],
                [0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,0],
                [0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0],
                [0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0],
                [0,1,1,0,0,1,1,1,0,1,0,1,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


status_success = numpy.array(status_success)
status_fail = numpy.array(status_fail)

try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        while True:
            for y in range(16):
              for x in range(16):
                h = 0.0
                s = 1.0
                v = status_fail[x,y]
                rgb = colorsys.hsv_to_rgb(h, s, v)
                r = int(rgb[0]*255.0)
                g = int(rgb[1]*255.0)
                b = int(rgb[2]*255.0)
                unicorn.set_pixel(x, y, r, g, b)
            unicorn.show()
            time.sleep(0.005)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        while True:
            for y in range(16):
              for x in range(16):
                h = 0.0
                s = 1.0
                v = status_fail[x,y]
                rgb = colorsys.hsv_to_rgb(h, s, v)
                r = int(rgb[0]*255.0)
                g = int(rgb[1]*255.0)
                b = int(rgb[2]*255.0)
                unicorn.set_pixel(x, y, r, g, b)
            unicorn.show()
            time.sleep(0.005)
else:
    print(response.getcode())
    while True:
        for y in range(16):
          for x in range(16):
            h = 0
            s = 255.0
            v = status_success[x,y]
            rgb = colorsys.hsv_to_rgb(h, s, v)
            r = int(rgb[0]*255.0)
            g = int(rgb[1]*255.0)
            b = int(rgb[2]*255.0)
            unicorn.set_pixel(x, y, r, g, b)
        unicorn.show()
        time.sleep(0.005)

