# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pyrealsense2 as rs
import serial
import time

data = serial.Serial('com6',9600)
            
def led_on():                           
    data.write(b'1')
                    
def led_off():
    data.write(b'0')
    
p = rs.pipeline()                                                       #establishing connection with the realsense depth cam
p.start()

def getinfo():
    frames = p.wait_for_frames()
    depth = frames.get_depth_frame()
    width = depth.get_width()
    height = depth.get_height()                                         #receiving depth info
    print (width, " ", height)
    dist_to_center = depth.get_distance(int(width/2), int(height/2))    #getting dist from middle pixel for testing
    print (dist_to_center)
    led_on()
    return dist_to_center


dist = getinfo()

while True:
    while dist > 1:
        time.sleep(0.5)
        dist = getinfo()

    else:
        led_off()
        time.sleep(1)
        dist = getinfo()


p.stop()


