# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:15:15 2020

@author: engka
"""

import pyrealsense2 as rs
import time

p = rs.pipeline()                                                       #establishing connection with the realsense depth cam
p.start()

p = rs.pipeline()                                                       #establishing connection with the realsense depth cam
p.start()

h = 240

def get_info(h):
    frames = p.wait_for_frames()
    depth = frames.get_depth_frame()                                   #receiving depth info
    o_point1 = depth.get_distance(240, h)    #getting dist from middle pixel for testing
    o_point2 = depth.get_distance(330, h)
    o_point3 = depth.get_distance(420, h)
    o_point4 = depth.get_distance(510, h)
    o_point5 = depth.get_distance(608, h)
    
    j_point1 = depth.get_distance(200,50)
    j_point2 = depth.get_distance(200,150)
    j_point3 = depth.get_distance(648,50)
    j_point4 = depth.get_distance(648,150)
    
    j_point5 = depth.get_distance(230,50)
    j_point6 = depth.get_distance(230,150)
    j_point7 = depth.get_distance(618,50)
    j_point8 = depth.get_distance(618,150)
    
    j_L1 = j_point5 - j_point1
    j_L2 = j_point6 - j_point2
    j_R1 = j_point7 - j_point3
    j_R2 = j_point8 - j_point4
    print ('Obstacle Depth:', o_point3, '\nJunction depth diff:', j_L2, j_R2)
    return o_point1, o_point2, o_point3, o_point4, o_point5, j_L1, j_L2, j_R1, j_R2

o_point1, o_point2, o_point3, o_point4, o_point5, j_L1, j_L2, j_R1, j_R2 = get_info(h)

def obstacle(o_point1, o_point2, o_point3, o_point4, o_point5):
    if (o_point1 <1 and o_point1 != 0) or (o_point2 <1 and o_point2 !=0) or (o_point3 < 1 and o_point3 != 0) or (o_point4 < 1 and o_point4 !=0) or (o_point5 <1 and o_point5 !=0):
        print ('Obstacle Detected!')
        return 0
    
def junction(j_L1, j_L2, j_R1, j_R2):
    if (j_L1 > 0.7 and j_L2 > 0.7) or (j_R1 > 0.7 and j_R2 > 0.7):
        print ('Junction Detected!')
        return 0

try:
    while True:
        movement1 = obstacle(o_point1, o_point2, o_point3, o_point4, o_point5)
        movement2 = junction(j_L1, j_L2, j_R1, j_R2)
        if movement1 == 0 or movement2 == 0:
           # o_point1, o_point2, o_point3, o_point4, o_point5, j_L1, j_L2, j_R1, j_R2 = get_info(w,h)
            time.sleep(5)
            o_point1, o_point2, o_point3, o_point4, o_point5, j_L1, j_L2, j_R1, j_R2 = get_info(h)
        else:
            time.sleep(0.2)
            o_point1, o_point2, o_point3, o_point4, o_point5, j_L1, j_L2, j_R1, j_R2 = get_info(h)
finally:
    p.stop()
        