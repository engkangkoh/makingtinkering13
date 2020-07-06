# -*- coding: utf-8 -*-
"""

@author: engkang
"""

import pyrealsense2 as rs                                           #importing realsense library

p = rs.pipeline()                                                   #establishing connection with the realsense depth cam
p.start()

frames = p.wait_for_frames()
depth = frames.get_depth_frame()                                    #receiving depth info
width = depth.get_width()           
height = depth.get_height()
print (width, " ", height)
dist_to_center = depth.get_distance(int(width/2), int(height/2))    #getting dist from middle pixel for testing
print (dist_to_center)
