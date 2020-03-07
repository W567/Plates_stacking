import sys
import WorkspaceDirInfo as wd

classesDir = wd.WorkspaceDir + "share/tools/classes"
sys.path.append(classesDir)

from realsenseD435Settings import *

ExampleSetting = realsenseD435SettingsClass(gColorFormat['RGB8'],
                                            gColorResolution['res960x540'],
                                            gColorFrameRate['6'],
                                            gDepthAndIR_Resolution['res1280x720'],
                                            gDepthAndIR_FrameRate['30'],
                                            gDepthFormat['Z16'],
                                            gIR_Format['Y8'])
