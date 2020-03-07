#!/usr/bin/env python
# -*- Python -*-
import sys
import os
import time
import copy
import threading
import numpy as np
pi = np.pi

#import world path ===================
import WorkspaceDirInfo as shareDir
sys.path.append(shareDir.WorkspaceDir)

import share.tools.geo.geo as geo
from share.tools.classes.f21pa10Class import fpa10Class
from share.tools.classes.parallelGripperClass import parallelGripperClass

#import local path ===================
sys.path.append(os.path.join(".."))
import set_env
baseDir = shareDir.WorkspaceDir + set_env.MyName
sys.path.append(baseDir)


# ========================================================================================================
#
#         instance
#
# ========================================================================================================
arm_r = fpa10Class("_r")
arm_l = fpa10Class("_l") 

world_l = [0.65, -0.4, 0.023, 0, 0, 0]
arm_l.coordMode_Table(world_l)

world_r = [0.65, 0.4, 0.02, 0, 0, 0]
arm_r.coordMode_Table(world_r)

import visual
visual.scene.center = (-0.6,0,0.3)

# ========================================================================================================
#
#         instance
#
# ========================================================================================================
def move_world_pa10(arm = arm_r ):
    
    base_xyzabc = [-0.1, 0.0, 0.2, 0, 0, 0]
    div_d = 0.05
    div_ang = 20 * pi /180
    
    # change mode joint  and  move ready pose
    print "mode joint"
    arm.mode_joint()
     
    print "move ready"
    arm.move_ready()
      
    # wait 1 sencond
    time.sleep(1)
    
    # change mode rmrc and move xyz
    print "mode rmrc"
    arm.mode_rmrc()
    print "move xyz"
    j = base_xyzabc[:]
    arm.move_rmrc(j)
    j[1] -= div_d
    arm.move_rmrc(j)
    j[1] += div_d
    j[0] += div_d
    arm.move_rmrc(j)
    j[1] += div_d
    j[0] -= div_d
    arm.move_rmrc(j) 
    j = base_xyzabc[:]
    arm.move_rmrc(j)

    
    # move abc
    print "move abc"
    j[3] += div_ang
    arm.move_rmrc(j)
    j[3] -= div_ang
    j[4] += div_ang
    arm.move_rmrc(j)
    j[3] -= div_ang
    j[4] -= div_ang
    arm.move_rmrc(j) 
    j = base_xyzabc[:]
    arm.move_rmrc(j)
    
    # change mode joint  and  move ready pose
    print "mode joint"
    arm.mode_joint()
     
    print "move ready"
    arm.move_ready()
    
def fmove_world_pa10(arm = arm_l ):
    
    base_xyzabc = [0.0, 0.0, 0.2, 0, 0, 0]
    div_z  = 0.2 
    reset_force_time = 1.0
    
    # change mode rmrc and move xyz
    arm.mode_rmrc()
    
    j = base_xyzabc[:]
    j[2] += div_z
    arm.move_rmrc(j)
    
    # ============== arm force sensor offset reset ==============
    time.sleep(reset_force_time)    
    arm.otc_setFOffset()    
    time.sleep(reset_force_time)
    
    # confirm force sensor value ----
    arm.getState()
    if (arm.f_now[2] > 0.3) or (arm.f_now[2] < -0.3):    
        print "force sensor value error"
        return False
    
    # ============== move  on Table =============================
    fj = base_xyzabc[:]
    fj[2] += arm.F_F
    arm.mode_fMove()
    arm.move_fMoveLim(fj, 1.0, force=5.0)
    
    # change mode joint  and  move ready pose
    print "mode joint"
    arm.mode_joint()
     
    print "move ready"
    arm.move_ready()