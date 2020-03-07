import sys
import os
import time
import json

### for find chess board corners ###
import cv2

### for newton algorithm ###
import numpy as np
from numpy.linalg import svd
from numpy.linalg import inv

from visual import *
#from dirspec import basedir
scene.center = (0, 0, 0)
scene.forward = (-1, 0, 0)
scene.up = (0, 0, 1)
scene.ambient = 0.6

#import world path ===================
import WorkspaceDirInfo as shareDir
sys.path.append(shareDir.WorkspaceDir)

import share.tools.geo.geo as geo
from share.tools.geo.object_model_v import CoordinateObject

### function json #############################################################
def json_read( filePath ):
    
    f = open(filePath, "r")
    json_data = json.load(f)
    f.close()
    
    return json_data
    
def json_write(dict, filePath):
    
    f = open(filePath, "w")
    json.dump(dict, f, indent=4 )
    f.close()
    
### functions for newton algorithm #############################################################
def cvt_FRAME2npmat(frm):
    npmat = np.matrix([ 
                    [frm.mat[0][0], frm.mat[0][1], frm.mat[0][2], frm.vec[0] ],
                    [frm.mat[1][0], frm.mat[1][1], frm.mat[1][2], frm.vec[1] ],
                    [frm.mat[2][0], frm.mat[2][1], frm.mat[2][2], frm.vec[2] ],
                    [0.0, 0.0, 0.0 , 1.0]
                    ])
    return npmat


def cvt_npmat2FRAME(npmat):
    frm = geo.FRAME(
            mat=[
                [ npmat[0, 0], npmat[0, 1], npmat[0, 2] ],
                [ npmat[1, 0], npmat[1, 1], npmat[1, 2] ],
                [ npmat[2, 0], npmat[2, 1], npmat[2, 2] ]
                ],
            vec=[ npmat[0, 3], npmat[1, 3], npmat[2, 3] ])
    return frm


def calc_Ttool2c_kplus1(Ttool2c_k, q):  # ## t_c is indix[0:5] of q
    t_c = np.matrix([
                          [1., 0., 0., q[0, 0]],
                          [0., 1., 0., q[1, 0]],
                          [0., 0., 1., q[2, 0]],
                          [0., 0., 0., 1.]])

    alpha_c = np.matrix([[1., 0., 0., 0.],
                         [0., np.cos(q[3, 0]), -np.sin(q[3, 0]), 0.],
                         [0., np.sin(q[3, 0]), np.cos(q[3, 0]), 0.],
                         [0., 0., 0., 1.]])
    beta_c = np.matrix([
                         [np.cos(q[4, 0]), 0., np.sin(q[4, 0]), 0.],
                         [0., 1., 0., 0.],
                         [-np.sin(q[4, 0]), 0., np.cos(q[4, 0]), 0.],
                         [0., 0., 0., 1.]])
    gamma_c = np.matrix([
                          [np.cos(q[5, 0]), -np.sin(q[5, 0]), 0., 0.],
                          [np.sin(q[5, 0]), np.cos(q[5, 0]), 0., 0.],
                          [0., 0., 1., 0.],
                          [0., 0., 0., 1.]]);

    Ttool2c_kplus1 = Ttool2c_k * t_c * alpha_c * beta_c * gamma_c

    return Ttool2c_kplus1


def calc_Tb2cb_kplus1(Tb2cb_k, q):  # ## t_cb is indix[6:11] of q
    t_cb = np.matrix([[1., 0., 0., q[6, 0]],
                          [0., 1., 0., q[7, 0]],
                          [0., 0., 1., q[8, 0]],
                          [0., 0., 0., 1.]])

    alpha_cb = np.matrix([
                          [1., 0., 0., 0.],
                          [0., np.cos(q[9, 0]), -np.sin(q[9, 0]), 0.],
                          [0., np.sin(q[9, 0]), np.cos(q[9, 0]), 0.],
                          [0., 0., 0., 1.]])
    
    beta_cb = np.matrix([
                          [np.cos(q[10, 0]), 0., np.sin(q[10, 0]), 0.],
                          [0., 1., 0., 0.],
                          [-np.sin(q[10, 0]), 0., np.cos(q[10, 0]), 0.],
                          [0., 0., 0., 1.]])
    
    gama_cb = np.matrix([
                          [np.cos(q[11, 0]), -np.sin(q[11, 0]), 0., 0.],
                          [np.sin(q[11, 0]), np.cos(q[11, 0]), 0., 0.],
                          [0., 0., 1., 0.],
                          [0., 0., 0., 1.]]);

    Tb2cb_kplus1 = Tb2cb_k * t_cb * alpha_cb * beta_cb * gama_cb 

    return Tb2cb_kplus1


def calc_projectionError_handCam(Tb2cb_k, Ttool2c_k, Tb2tool, Pcb, Pc, num):
    # initialize a num*3x1 matrix which is returned
    tmp = []
    for i in range(0, num * 3):
        tmp.append(0.)
    ret = np.matrix([tmp]).transpose()

    # the equations
    y = []  # list of equations
    j = 0
    count_p = 0
    viz_point = []
    for i in range(0, num):
        if i % 4 == 0:
            Tb2tool_j = Tb2tool[j]
            j = j + 1

        y.append((Tb2cb_k * Pcb[i]) - (Tb2tool_j * Ttool2c_k * Pc[i]))
        ### projection visualizer ###
        Pcb_ = Tb2cb_k * Pcb[i]
        Pc_ = Tb2tool_j * Ttool2c_k * Pc[i]
        viz_point.append(visual.points(pos=[ (Pcb_.item((0, 0)), Pcb_.item((1, 0)), Pcb_.item((2, 0))) ], size=10, color=color.red))
        viz_point.append(visual.points(pos=[ (Pc_.item((0, 0)) , Pc_.item((1, 0)) , Pc_.item((2, 0))) ], size=10, color=color.cyan))
        
        count_p = count_p + 1
        if count_p == 4:
            count_p = 0     
            raw_input()  #--------------------------------
            for v in viz_point:
                 v.visible = False
                 del v
    
    # create return matrix
    for i in range(0, num):
        for j in range(0, 3):
            ret[i * 3 + j, 0] = y[i][j, 0]
            
    return  ret


def calc_jacobien_handCam(Tb2cb_k, Ttool2c_k, Tb2tool, Pcb, Pc, num):
    # initialize a num*3x1 matrix which is returned
    tmp = []
    for i in range(0, num * 3):
        tmp.append([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
    Jacob = np.matrix(tmp)

    dx = np.matrix([
                 [ 0.0, 0.0, 0.0, 1.0],
                 [ 0.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0]
                 ])
    dy = np.matrix([
                 [ 0.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 1.0],
                 [ 0.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0]
                 ])
    dz = np.matrix([
                 [ 0.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 1.0],
                 [ 0.0, 0.0, 0.0, 0.0]
                 ])
    dalpha = np.matrix([
                 [ 0.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, -1.0, 0.0],
                 [ 0.0, 1.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0]
                 ])
    dbeta = np.matrix([
                 [ 0.0, 0.0, 1.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0],
                 [-1.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0]
                 ])
    dgamma = np.matrix([
                 [ 0.0, -1.0, 0.0, 0.0],
                 [ 1.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0]
                 ])

    l = 0
    for i in range(0, num):
        w = []
        if i % 4 == 0:
            Tb2tool_l = Tb2tool[l]
            l = l + 1
               
        # df/dx_c
        w.append(-(Tb2tool_l * Ttool2c_k * dx * Pc[i]))
        # df/dy_c
        w.append(-(Tb2tool_l * Ttool2c_k * dy * Pc[i]))
        # df/dz_c
        w.append(-(Tb2tool_l * Ttool2c_k * dz * Pc[i]))
        
        # df/dalpha_c
        w.append(-(Tb2tool_l * Ttool2c_k * dalpha * Pc[i]))
        # df/dbeta_c
        w.append(-(Tb2tool_l * Ttool2c_k * dbeta * Pc[i]))
        # df/dgama_c
        w.append(-(Tb2tool_l * Ttool2c_k * dgamma * Pc[i]))
        
        # df/dx_cb
        w.append(Tb2cb_k * dx * Pcb[i])
        # df/dy_cb
        w.append(Tb2cb_k * dy * Pcb[i])
        # df/dz_cb
        w.append(Tb2cb_k * dz * Pcb[i])
       
        # df/dalpha_cb
        w.append(Tb2cb_k * dalpha * Pcb[i])
        # df/dbeta_cb
        w.append(Tb2cb_k * dbeta * Pcb[i])
        # df/dgama_cb
        w.append(Tb2cb_k * dgamma * Pcb[i])

        for j in range(0, 3):
            for k in range(0, 12):
                Jacob[i * 3 + j, k] = w[k][j, 0]

    return Jacob


def newton_handCam(frm_Tb2cb0, frm_Ttool2c0, frm_Tb2tool, Pcb, Pc, NUM):
    
    Ttool2c0 = cvt_FRAME2npmat(frm_Ttool2c0)
    Tb2cb0 = cvt_FRAME2npmat(frm_Tb2cb0)
    Tb2tool = []
    for t in frm_Tb2tool:
        Tb2tool.append(cvt_FRAME2npmat(t))
             
    #------------ this is for Visual ------------#V
    Ttool2c = cvt_FRAME2npmat(frm_Ttool2c0)
    Tb2cb = cvt_FRAME2npmat(frm_Tb2cb0)
    
    # global root
    coord_gl = CoordinateObject()
    coord_gl.unfix()
    coord_gl.set_trans(geo.FRAME(xyzabc=[0, 0, 0, 0, 0, 0]))
    coord_gl.vframe.set_visible(True)
    
    # base from chessboard0
    coord_bFromChessBoard = CoordinateObject()
    coord_bFromChessBoard.unfix()
    coord_bFromChessBoard.set_trans(frm_Tb2cb0)
    coord_bFromChessBoard.vframe.set_visible(True)
     
    # base from chessboard
    coord_bFromChessBoard0 = CoordinateObject()
    coord_bFromChessBoard0.unfix()
    coord_bFromChessBoard0.set_trans(frm_Tb2cb0)
    coord_bFromChessBoard0.vframe.set_visible(True)

    # base from cam
    coord_bFromCam = CoordinateObject()
    coord_bFromCam.unfix()
    coord_bFromCam.set_trans(frm_Tb2tool[0] * frm_Ttool2c0)
    coord_bFromCam.vframe.set_visible(True)

    #--------------------------------------------#V
    
    print "-----Ttool2c0----------\n"
    print Ttool2c0
    print "-----Tb2cb0----------\n"
    print Tb2cb0
    
    q0 = np.matrix([[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.]])
    Tb2cbk = Tb2cb0
    Ttool2ck = Ttool2c0
    for i in range(0, 50):
    
        #------------ this is for Visual ------------#V
        frm_Tb2cb = cvt_npmat2FRAME(Tb2cbk)
        frm_Ttool2c = cvt_npmat2FRAME(Ttool2ck)
        coord_bFromChessBoard.set_trans(frm_Tb2cb)
        coord_bFromCam       .set_trans(frm_Tb2tool[0] * frm_Ttool2c)
        #--------------------------------------------#V
        
        time_pre = time.time()
        
        q = q0
        e = calc_projectionError_handCam(Tb2cbk, Ttool2ck, Tb2tool, Pcb, Pc, NUM)
#         #create fake projection error for debug 
#         e = ndarray([1,2,3,4])
#         e.resize((NUM*3, 1))
#         #resize( e ,(NUM*3, 1) )
#         #print e
#         for i in range(0,NUM/4):
#             x = 0.00
#             y = 0.00
#             z = 0.00
#             alpha = 0.00 *pi
#             beta  = 0.00 *pi
#             gamma = 0.00 *pi
#               
#             points_a  = []
#             points_a.append(geo.VECTOR(0.0, 0.0, 0.0))
#             points_a.append(geo.VECTOR(0.0, 0.3, 0.0))
#             points_a.append(geo.VECTOR(0.3, 0.0, 0.0))
#             points_a.append(geo.VECTOR(0.3, 0.3, 0.0))
#               
#             points_b = []
#             points_b.append( geo.FRAME(xyzabc = [x,y,z,alpha,beta,gamma]) * points_a[0] )
#             points_b.append( geo.FRAME(xyzabc = [x,y,z,alpha,beta,gamma]) * points_a[1] )
#             points_b.append( geo.FRAME(xyzabc = [x,y,z,alpha,beta,gamma]) * points_a[2] )
#             points_b.append( geo.FRAME(xyzabc = [x,y,z,alpha,beta,gamma]) * points_a[3] )
#               
#             points_diff=[]
#             points_diff.append( points_a[0] - points_b[0] )
#             points_diff.append( points_a[1] - points_b[1] )
#             points_diff.append( points_a[2] - points_b[2] )
#             points_diff.append( points_a[3] - points_b[3] )
#               
#             #p0
#             point =0
#             e[3*4*i+point*3+0, 0] = points_diff[0][0]
#             e[3*4*i+point*3+1, 0] = points_diff[0][1]
#             e[3*4*i+point*3+2, 0] = points_diff[0][2]
#             #p1
#             point =1
#             e[3*4*i+point*3+0, 0] = points_diff[1][0]
#             e[3*4*i+point*3+1, 0] = points_diff[1][1]
#             e[3*4*i+point*3+2, 0] = points_diff[1][2]
#             #p2
#             point =2
#             e[3*4*i+point*3+0, 0] = points_diff[2][0]
#             e[3*4*i+point*3+1, 0] = points_diff[2][1]
#             e[3*4*i+point*3+2, 0] = points_diff[2][2]
#             #p3
#             point =3
#             e[3*4*i+point*3+0, 0] = points_diff[3][0]
#             e[3*4*i+point*3+1, 0] = points_diff[3][1]
#             e[3*4*i+point*3+2, 0] = points_diff[3][2]
#         print e
        
        jacob = calc_jacobien_handCam(Tb2cbk, Ttool2ck, Tb2tool, Pcb, Pc, NUM)
        U, sigma, V_trans = svd(jacob, compute_uv=1, full_matrices=0)
        q = -V_trans.T * np.diag(1.0 / sigma) * (U.T * e)
        
        Ttool2ck = calc_Ttool2c_kplus1(Ttool2ck, q)
        Tb2cbk = calc_Tb2cb_kplus1(Tb2cbk, q)
        
        time_post = time.time()
        time_diff = time_post - time_pre
        
        print ".", i, " ", time_diff
        sys.stdout.flush()
        
        raw_input()#------------------------------------
        
    print";"
    
    print "-----Ttool2c----------\n"
    print Ttool2ck
    print "-----Tb2cb----------\n"
    print Tb2cbk
    
    # -- calc residuals ------------------------------------------------#R
    err = calc_projectionError_handCam(Tb2cbk, Ttool2ck, Tb2tool, Pcb, Pc, NUM)
    e = zeros(NUM * 3)
    for i in range(0, NUM * 3):
        e[i] = err[i, 0]
    # MS[m] (mean square)
    meanSquare_error = np.sum(e * e) / (NUM * 3)
    # RMS[m] (root mean square)
    rootMeanSquare_error = sum(np.sqrt(e * e)) / (NUM * 3)
    # percentile[mm]
    min_error = 1000 * np.min(e)
    q1 = 1000 * np.percentile(e, 25.0)
    q2 = 1000 * np.percentile(e, 50.0)
    q3 = 1000 * np.percentile(e, 75.0)
    max_error = 1000 * np.max(e)
    # avsolute error percentile[mm]
    abs_e = np.abs(e)
    abs_min_error = 1000 * np.min(abs_e)
    abs_q1 = 1000 * np.percentile(abs_e, 25.0)
    abs_q2 = 1000 * np.percentile(abs_e, 50.0)
    abs_q3 = 1000 * np.percentile(abs_e, 75.0)
    abs_max_error = 1000 * np.max(abs_e)

    # print "error list:"
    # print e
    # print "mean square of error:"
    # print meanSquare_error
    print "\n-- residuals evaluation --------------------"
    print "root mean square of error [mm]:"
    print rootMeanSquare_error * 1000, "\n"
    print "percentile(0, 25, 50, 75, 100%) of error [mm]:"
    print " min : ", min_error
    print " 25% : ", q1
    print " 50% : ", q2
    print " 75% : ", q3
    print " max : ", max_error, "\n"
    print "percentile(0, 25, 50, 75, 100%) of absolute error [mm]:"
    print " min : ", abs_min_error
    print " 25% : ", abs_q1
    print " 50% : ", abs_q2
    print " 75% : ", abs_q3
    print " max : ", abs_max_error
    
    print "(error is distances of reprojection error of points on chessboared)"
    # -- calc residuals ------------------------------------------------#R
    
    return Tb2cbk, Ttool2ck
    
end_helper_func = 1
############################################################# functions for newton algorithm ###



def execute_calib():
  
    ### get Tc2cb ###################################################################################################
  

    argvs = sys.argv
    argc = len(argvs)
    if(argc != 2):
        print "Usage : handCamCalibdata.json !!!"
        quit()

    jdata = json_read(argvs[1])
    print " -------------- read json data ---------------------"
    
    plist_handCamCalib = jdata["plist_handCamCalib"]
    listTf_Tc2cb = jdata["listTf_Tc2cb"]
    Th2tool_handCamCalib = geo.FRAME(xyzabc=jdata["Th2tool_handCamCalib_xyzabc"])
    Th2c_handCam = geo.FRAME(xyzabc=jdata["Th2c_handCam_xyzabc"])
    
    list_Tf = []
    for d in listTf_Tc2cb :
        list_Tf.append(np.matrix(d))
    
    print "plist_handCamCalib : ", plist_handCamCalib
    print "list_Tf : ", list_Tf
    print "Th2tool_handCamCalib", Th2tool_handCamCalib
    print "Th2c_handCam", Th2c_handCam
    
    Tc2cb = []
    Tb2tool = []
    for i in range(len(plist_handCamCalib)):
        Tc2cb.append(cvt_npmat2FRAME(list_Tf[i]))
        Tb2tool.append(geo.FRAME(xyzabc=plist_handCamCalib[i]))
            
    ################################################################################################### get Tc2cb ###
        
        
    ### get Tb2tool #########################################################################    
#     Tb2tool = []
#     for p in conf.plist_handCamCalib:
#         Tb2tool.append(geo.FRAME(xyzabc=p))
    ######################################################################### get Tb2tool ###
    
    Ttool2c_handCraft_wrtTool = -Th2tool_handCamCalib * Th2c_handCam
    Tb2h0 = Tb2tool[0] * -Th2tool_handCamCalib
    Tb2c0 = Tb2tool[0] * Ttool2c_handCraft_wrtTool
    Tb2cb0 = Tb2tool[0] * Ttool2c_handCraft_wrtTool * Tc2cb[0]
    
    Points_onChessBoard = []  # size of this will be 4*scene.
    for p in Tb2tool:
        Points_onChessBoard.append(np.matrix([ [0.0], [0.0], [0.0], [1.0] ]))
        Points_onChessBoard.append(np.matrix([ [0.3], [0.0], [0.0], [1.0] ]))
        Points_onChessBoard.append(np.matrix([ [0.0], [0.3], [0.0], [1.0] ]))
        Points_onChessBoard.append(np.matrix([ [0.3], [0.3], [0.0], [1.0] ]))           
    
    Points_fromCam = []  # size of this will be 4*scene.
    for c in Tc2cb:
        p0 = c * geo.VECTOR(0.0, 0.0, 0.0)
        Points_fromCam.append(np.matrix([ [p0[0]], [p0[1]], [p0[2]], [1.] ]))
        p1 = c * geo.VECTOR(0.3, 0.0, 0.0)
        Points_fromCam.append(np.matrix([ [p1[0]], [p1[1]], [p1[2]], [1.] ]))
        p2 = c * geo.VECTOR(0.0, 0.3, 0.0)
        Points_fromCam.append(np.matrix([ [p2[0]], [p2[1]], [p2[2]], [1.] ]))
        p3 = c * geo.VECTOR(0.3, 0.3, 0.0)
        Points_fromCam.append(np.matrix([ [p3[0]], [p3[1]], [p3[2]], [1.] ]))
           
    
    # global root
    coord_gl = CoordinateObject()
    coord_gl.unfix()
    coord_gl.set_trans(geo.FRAME(xyzabc=[0, 0, 0, 0, 0, 0]))
    coord_gl.vframe.set_visible(True)
    
#     # cam to cb0
#     coord_cam2cb0 = CoordinateObject()
#     coord_cam2cb0.unfix()
#     coord_cam2cb0.set_trans( Tc2cb[0] )
#     coord_cam2cb0.vframe.set_visible(True)
    
    
#     # base to tool
#     coord_bFromTool0 = CoordinateObject()
#     coord_bFromTool0.unfix()
#     coord_bFromTool0.set_trans( Tb2tool[0] )
#     coord_bFromTool0.vframe.set_visible(True)

    # base to hand0
    coord_b2h0 = CoordinateObject()
    coord_b2h0.unfix()
    coord_b2h0.set_trans(Tb2h0)
    coord_b2h0.vframe.set_visible(True)

    # base to camera0
    coord_b2cam0 = CoordinateObject()
    coord_b2cam0.unfix()
    coord_b2cam0.set_trans(Tb2c0)
    coord_b2cam0.vframe.set_visible(True)

    # base to cb0
    coord_b2cb0 = CoordinateObject()
    coord_b2cb0.unfix()
    coord_b2cb0.set_trans(Tb2cb0)
    coord_b2cb0.vframe.set_visible(True)

    raw_input()
    Tb2cb, Ttool2c = newton_handCam(Tb2cb0, Ttool2c_handCraft_wrtTool, Tb2tool , Points_onChessBoard, Points_fromCam, len(Tb2tool) * 4)

    print "Tb2cb : ", Tb2cb
    print "Ttool2c : ", Ttool2c
    
#     Th2tool = conf.Th2tool_handCamCalibCalc * geo.FRAME(xyzabc=[0, 0, 0, 0, 0.99999 * pi, 0]) 
    Th2c = cvt_FRAME2npmat(Th2tool_handCamCalib) * Ttool2c 

    # -- output to file Tb2cb.py ----------------------------------------------------#O
    fp = open("Th2c.py", "w");
    fp.write("import sys\n");
    fp.write("import WorkspaceDirInfo as shareDir\n");
    fp.write("sys.path.append(shareDir.WorkspaceDir)\n");
    fp.write("import share.tools.geo.geo as geo\n");
    fp.write("Th2c=geo.FRAME(mat=[[%f,%f,%f],[%f,%f,%f],[%f,%f,%f]],vec=[%f,%f,%f])"\
            % (Th2c[0, 0], Th2c[0, 1], Th2c[0, 2], \
            Th2c[1, 0], Th2c[1, 1], Th2c[1, 2], \
            Th2c[2, 0], Th2c[2, 1], Th2c[2, 2], \
            Th2c[0, 3], Th2c[1, 3], Th2c[2, 3]));
    fp.close();
    print "ttee"
    #------------------------------------------------------------------------------#O
    
if __name__ == "__main__":
    execute_calib()
    scene.exit = True
    exit()