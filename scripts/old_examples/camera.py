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

#import local path ===================
sys.path.append(os.path.join(".."))
import set_env
baseDir = shareDir.WorkspaceDir + set_env.MyName
sys.path.append(baseDir)

from share.tools.classes.realsenseClass import realsenseClass

# ========================================================================================================
#
#         instance
#
# ========================================================================================================
realsense = realsenseClass()

# ========================================================================================================
#
#         instance
#
# ========================================================================================================
    
