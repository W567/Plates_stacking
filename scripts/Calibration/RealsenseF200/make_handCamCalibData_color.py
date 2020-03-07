import sys
import os
import time
import copy
import threading
import numpy as np
import json
import cv2
import xml.etree.ElementTree as xmlEt
from math import pi

#import world path ===================
import WorkspaceDirInfo as shareDir
sys.path.append(shareDir.WorkspaceDir)

import share.tools.geo.geo as geo

#import local path ===================
sys.path.append(os.path.join("..", ".."))
import set_env
baseDir = shareDir.WorkspaceDir + set_env.MyName
sys.path.append(baseDir)

import myPyUtil as myUtil

### define Chessboard information ###
CHESS_SIZE = (10, 7)
CHESS_SQUARE_SIZE = 12.8  # [mm]

### path of camera parameter #####################
PATH_CAM_PARAM = shareDir.WorkspaceDir + "share/data/RealSense/RealSense-02/intrinsic_Color.xml"
PATH_IMAGE_DATA = baseDir + "/data/handCamCalib/"
TITLE = "picture"
EXTENSION = ".png"
JSON_DATA_NAME = "handCamCalibData_color.json"

### Transform HAND to CAMERA as initial value ##################
Th2c_handCam_xyzabc = [
        - 0.090,  # [m]
         0.000,  # [m]
         0.135,  # 0.033, #[m]
         0.00 * pi,  # rotation around x axis [rad]
         0.00 * pi,  # rotation around y axis [rad]
        - 0.50 * pi  # rotation around z axis [rad]
        ]
Th2c_handCam = geo.FRAME(xyzabc=Th2c_handCam_xyzabc)

### Tranform HAND to TOOL TIP for calib mortion ###
Th2tool_handCamCalib_xyzabc = [ 
        -0.086,
        0.00,
        0.50,
        0.00 * pi,
        0.99999999 * pi,
        0.00 * pi]
# Th2tool_handCamCalib_xyzabc = [ 
#         0.00,
#         0.00,
#         0.227,
#         0.00 * pi,
#         0.99999999 * pi,
#         0.00 * pi])
Th2tool_handCamCalib = geo.FRAME(xyzabc=Th2tool_handCamCalib_xyzabc)

### motion conf ################################################
x = 0.7
y = 0.0
z = 0.0
 
plist_handCamCalib = []
plist_handCamCalib.append([x, y, z, 0.20 * pi, 0, 0.4 * pi])
plist_handCamCalib.append([x, y, z, 0.1 * pi, 0, -0.3 * pi])
plist_handCamCalib.append([x, y, z, -0.00 * pi, 0, 0.2 * pi ])
plist_handCamCalib.append([x, y, z, -0.1 * pi, 0, -0.4 * pi])
plist_handCamCalib.append([x, y, z, -0.2 * pi, 0, 0.3 * pi])
 
plist_handCamCalib.append([x, y, z, 0.15 * pi, 0.05 * pi, -0.4 * pi])
plist_handCamCalib.append([x, y, z, 0.075 * pi, 0.025 * pi, 0.2 * pi])
plist_handCamCalib.append([x, y, z, -0.00 * pi, 0.05 * pi, -0.2 * pi])
plist_handCamCalib.append([x, y, z, -0.075 * pi, -0.1 * pi, 0.1 * pi])
plist_handCamCalib.append([x, y, z, -0.15 * pi, -0.05 * pi, -0.3 * pi])
  
plist_handCamCalib.append([x, y, z, 0.15 * pi, -0.1 * pi, -0.4 * pi])
plist_handCamCalib.append([x, y, z, 0.075 * pi, -0.05 * pi, -0.2 * pi])
plist_handCamCalib.append([x, y, z, -0.00 * pi, -0.1 * pi, 0.1 * pi])
plist_handCamCalib.append([x, y, z, -0.075 * pi, 0.05 * pi, -0.1 * pi])
plist_handCamCalib.append([x, y, z, -0.15 * pi, 0.1 * pi, 0.1 * pi])

# x = 0.68
# y = -0.10
# z = 0.15
# a = 60*pi/180
# b = 0*pi/180
# c = 0*pi/180
# plist_handCamCalib = []
# plist_handCamCalib.append([x, y, z, a, b, c])
# plist_handCamCalib.append([x+0.05, y, z, a, b, c])
# plist_handCamCalib.append([x-0.05, y, z, a, b, c])
# plist_handCamCalib.append([x, y+0.05, z, a, b, c])
# plist_handCamCalib.append([x+0.03, y+0.05, z, a, b, c])
# plist_handCamCalib.append([x-0.03, y+0.05, z, a, b, c])
# 
# x = 0.68
# y = 0.17
# z = 0.12
# a = -60*pi/180
# b = 0*pi/180
# c = 0*pi/180
# plist_handCamCalib.append([x, y, z, a, b, c])
# plist_handCamCalib.append([x+0.05, y, z, a, b, c])
# plist_handCamCalib.append([x-0.05, y, z, a, b, c])
# plist_handCamCalib.append([x, y-0.03, z, a, b, c])
# plist_handCamCalib.append([x+0.03, y-0.03, z, a, b, c])
# plist_handCamCalib.append([x-0.03, y-0.03, z, a, b, c])
#  
# x = 0.72
# y = 0.01
# z = 0.2
# a = 0*pi/180
# b = -60*pi/180
# c = 0.99999999*pi
# plist_handCamCalib.append([x, y, z, a, b, c])
# plist_handCamCalib.append([x, y+0.03, z, a, b, c])
# plist_handCamCalib.append([x, y-0.03, z, a, b, c])
# plist_handCamCalib.append([x-0.05, y, z, a, b, c])
# plist_handCamCalib.append([x-0.05, y+0.05, z, a, b, c])
# plist_handCamCalib.append([x-0.05, y-0.05, z, a, b, c])

# plist_handCamCalibData = []
def json_read( filePath ):
    
    f = open(filePath, "r")
    json_data = json.load(f)
    f.close()
    
    return json_data
    
def json_write(dict, filePath):
    
    f = open(filePath, "w")
    json.dump(dict, f, indent=4 )
    f.close()
    
    
def move_calib():
    
    from share.tools.classes.f21pa10Class import fpa10Class
    from tools.classes.realsenseClass import realsenseClass

    camera = realsenseClass()
    arm = fpa10Class("_l")
    
    arm.Th2tool = Th2tool_handCamCalib
    arm.otc_setToolOffset([arm.Th2tool.vec[0], arm.Th2tool.vec[1], arm.Th2tool.vec[2]])
    
    arm.mode_joint()
    arm.move_joint(arm.j_ready)
    
    arm.mode_rmrc()
    time.sleep(1)
    
    plistData = []
    
    for i in range(len(plist_handCamCalib)):
        raw_input("press Enter to move next point >>")
        arm.move_rmrc(plist_handCamCalib[i])
        
        title = TITLE + str(i) + EXTENSION;
        time.sleep(1)
        camera.update_image(camera.COLOR)
        time.sleep(1)
        camera.save_image(PATH_IMAGE_DATA + title, camera.COLOR)
        plistData.append(arm.t_xyzabc_now)
        
    raw_input("finished. press Enter to back to ready position")
    arm.mode_joint()
    arm.move_joint(arm.j_ready)

    data = {"plistData" : plistData}
    
    json_write(data, PATH_IMAGE_DATA+"plistData.json" )
    
    
def calc_extrinsic(tuple_chessSize, chessSquareSize, list_img, camParam, distortion):
 
    # cvWindow = cv2.namedWindow( "cv_window" )
 
    # create object points
    objPoints = []
    for i in range(0, tuple_chessSize[1]):
        for j in range(0, tuple_chessSize[0]):
            objPoints.append((i * chessSquareSize, j * chessSquareSize, 0))
    objPoints = np.array(objPoints)

    list_Tf = []
    list_accept = []
    counter = 0
    # process each images
    for img in list_img:
        print "img : %d" % counter
        # cvt img BGR to GRAY
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # find chesscoard corners
        found, corners = cv2.findChessboardCorners(gray, tuple_chessSize)
        if found:
            # find corner sub pix
            cv2.cornerSubPix(
                 image=gray,
                 corners=corners,
                 winSize=(5, 5),
                 zeroZone=(-1, -1),
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 30, 0.01))
            
            # calc extrinsic    
            found, r_vec, t_vec = cv2.solvePnP(
                 objectPoints=objPoints,
                 imagePoints=corners,
                 cameraMatrix=camParam,
                 distCoeffs=distortion)
            
            r_mtx, scratch = cv2.Rodrigues(r_vec)
            Tf = np.matrix([
                            [r_mtx[0, 0], r_mtx[0, 1], r_mtx[0, 2], t_vec[0, 0] * 0.001 ],
                            [r_mtx[1, 0], r_mtx[1, 1], r_mtx[1, 2], t_vec[1, 0] * 0.001 ],
                            [r_mtx[2, 0], r_mtx[2, 1], r_mtx[2, 2], t_vec[2, 0] * 0.001 ],
                            [        0., 0., 0., 1. ],  # t_vec is converted [mm]->[m]
                            ])
               
            list_Tf.append(Tf.tolist())
            list_accept.append(True)
            print "Transform"
            print Tf
            
        else:
            list_Tf.append(None)
            list_accept.append(False)
            print "FAILED to fined corner" 
        
        print ""
        cv2.drawChessboardCorners(img, tuple_chessSize, corners, found)
        # cv2.imshow( "cv_window", img )
        # cv2.waitKey()
        #raw_input()#----------------------------------------------------------
        
        counter += 1
        
    # cv2.destroyWindow("cv_window")
    return list_Tf, list_accept

def make_jsonData():
    
    # make plist_handCamCalibData
    plistData = json_read(PATH_IMAGE_DATA+"plistData.json")
    plist_handCamCalibData = plistData["plistData"]
    print plist_handCamCalibData
    
    # make list image
    list_img = []
    list_inputFileName = []
    for i in range(len(plist_handCamCalibData)):
        title = PATH_IMAGE_DATA + TITLE + str(i) + EXTENSION
        list_inputFileName.append(title)
        list_img.append(cv2.imread(title))
    
    # ## load Intrinsic        
    handCam_intrinsic = xmlEt.parse(PATH_CAM_PARAM).getroot()
    camParam = myUtil.cvXml2cvNdarray(handCam_intrinsic.find("camera_matrix"))
    distortion = myUtil.cvXml2cvNdarray(handCam_intrinsic.find("distortion_coefficients"))
    
    print 'intrinsic'
    print handCam_intrinsic
    print '    camParam'
    print camParam
    print '    distortion'
    print distortion
    
    # ## calc extrinsics
    list_Tf, isAccepted = calc_extrinsic(
                                         CHESS_SIZE,
                                         CHESS_SQUARE_SIZE,
                                         list_img,
                                         camParam,
                                         distortion)
    
    print "%d images are accepted." % np.sum(isAccepted)
    print "list_Tf : ", list_Tf
    
    plist_handCamCalib = []
    listTf_Tc2cb = []
    for i, ret in enumerate(isAccepted):
        if(ret == True):
            plist_handCamCalib.append(plist_handCamCalibData[i])
            listTf_Tc2cb.append(list_Tf[i])
    
    jdata = {"plist_handCamCalib" : plist_handCamCalib,\
              "listTf_Tc2cb": listTf_Tc2cb, \
              "Th2tool_handCamCalib_xyzabc" : Th2tool_handCamCalib_xyzabc, \
              "Th2c_handCam_xyzabc" : Th2c_handCam_xyzabc
              }
    
    json_write(jdata, JSON_DATA_NAME)
    
    
    
    