import sys
import os
import time
import datetime 

import numpy as np
from math import pi

import xml.etree.ElementTree as xmlEt

#import world path ===================
import WorkspaceDirInfo as shareDir
sys.path.append(shareDir.WorkspaceDir)

import share.tools.geo.geo as geo

#import local path ===================
sys.path.append(os.path.join("..", ".."))
import set_env
baseDir = shareDir.WorkspaceDir + set_env.MyName
sys.path.append(baseDir)

def cvXml2cvNdarray( node ):
    rows = int( node.find("rows").text )
    cols = int( node.find("cols").text )
    data = map( float, node.find("data").text.split() )
    
    arr = np.asarray(data)
    arr = arr.reshape( rows, cols )
    return arr

def print_FRAME( f ):
    f6 = f.xyzabc()
    print "xyzabc[%7.4f, %7.4f, %7.4f ,%7.4f, %7.4f, %7.4f]" % (
        f6[0],
        f6[1],
        f6[2],
        f6[3],
        f6[4],
        f6[5])

def getVSize( v ): 
    return np.sqrt( v[0]*v[0] + v[1]*v[1] + v[2]*v[2] )

def getDateString():
    date = datetime.datetime.today()
    str_date = "__%s_%s_%s__%s_%s_%s" % (date.year,
                                        date.month,
                                        date.day,
                                        date.hour,
                                        date.minute,
                                        date.second)
    return str_date

def cvt_FRAME2npmat( frm ):
    npmat = np.matrix([ 
                    [frm.mat[0][0], frm.mat[0][1], frm.mat[0][2], frm.vec[0] ],
                    [frm.mat[1][0], frm.mat[1][1], frm.mat[1][2], frm.vec[1] ],
                    [frm.mat[2][0], frm.mat[2][1], frm.mat[2][2], frm.vec[2] ],
                    [0.0, 0.0, 0.0 ,1.0]
                    ])
    return npmat


def cvt_npmat2FRAME(npmat):
    frm = geo.FRAME( 
            mat = [
                [ npmat[0,0], npmat[0,1], npmat[0,2] ],
                [ npmat[1,0], npmat[1,1], npmat[1,2] ],
                [ npmat[2,0], npmat[2,1], npmat[2,2] ]
                ],
            vec = [ npmat[0,3], npmat[1,3], npmat[2,3] ] )
    return frm

