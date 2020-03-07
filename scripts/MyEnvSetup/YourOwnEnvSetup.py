# coding:utf-8
import sys
import numpy as np
import EnvSetupVar

import WorkspaceDirInfo as shareDir

shareToolsDir = shareDir.WorkspaceDir + "share/tools/"
geoDir = shareToolsDir + "geo/"
shareClassDir = shareToolsDir + "classes/"
CalibDataDir = shareDir.WorkspaceDir + "share/data/handCamCalib/"
baseDir = shareDir.baseDir
RTC_ClassDir = baseDir + "tools/classes/"

sys.path.append(shareDir.WorkspaceDir)
sys.path.append(geoDir)
sys.path.append(shareClassDir)
sys.path.append(baseDir)

import geo


def ConvertFRAME2mat(FRAME):
	if isinstance(FRAME, geo.FRAME):
		res = np.eye(4)
		res[:3, :3] = np.array(FRAME.mat)
		res[:3, 3] = np.array(FRAME.vec)
		return np.mat(res)
	else:
		print "EnvSetup.py ConvertFRAME2mat: Argument type is not geo.FRAME!"


# PA10 import
if EnvSetupVar.Need_PA10_L:
	from share.tools.classes.f21pa10Class import fpa10Class
	ARM_L = fpa10Class("_l")
	ARM_L.Load_Th2c()
	print "PA10_Left arm was created. Variable name is \"ARM_L\".\r\n"
elif EnvSetupVar.Need_PA10_R:
	from share.tools.classes.f21pa10Class import fpa10Class
	ARM_R = fpa10Class("_r")
	ARM_R.Load_Th2c()
	print "PA10_Right arm was created. Variable name is \"ARM_R\".\r\n"
elif EnvSetupVar.Need_PA10_BOTH:
	from share.tools.classes.f21pa10Class import fpa10Class
	ARM_L = fpa10Class("_l")
	ARM_L.Load_Th2c()
	print "PA10_Left arm was created. Variable name is \"ARM_L\".\r\n"

	ARM_R = fpa10Class("_r")
	ARM_R.Load_Th2c()
	print "PA10_Right arm was created. Variable name is \"ARM_R\".\r\n"

if EnvSetupVar.Need_PA10_IN_WORLD:
	EnvSetupVar.Tl2world = geo.FRAME(xyzabc=EnvSetupVar.Tl2world)
	if EnvSetupVar.Need_PA10_L:
		CoordArmL = (-EnvSetupVar.Tl2world)
		ARM_L.coordMode_Table(CoordArmL.xyzabc())
	elif EnvSetupVar.Need_PA10_R:
		tmp = (-EnvSetupVar.Tl2world)
		CoordArmR = tmp * fpa10Class.Tl2r
		ARM_R.coordMode_Table(CoordArmR.xyzabc())
	elif EnvSetupVar.Need_PA10_BOTH:
		Tl2r = geo.FRAME(xyzabc = (ARM_L.Tl2r.xyzabc()))
		CoordArmL = (-EnvSetupVar.Tl2world)
		ARM_L.coordMode_Table(CoordArmL.xyzabc())
		CoordArmR = (-EnvSetupVar.Tl2world) * Tl2r
		ARM_R.coordMode_Table(CoordArmR.xyzabc())
		import visual
		visual.scene.center = ((-EnvSetupVar.Tl2world).vec[0], (-EnvSetupVar.Tl2world).vec[1], (-EnvSetupVar.Tl2world).vec[2])


# Realsense import
if EnvSetupVar.Need_RealSense_L:
	select = 0
	try:
		ARM_L
	except NameError:
		select = raw_input("WARNING!!! No PA10_ARM_L created! Are you sure continue to create realsense instance?[y/N]")

	if select is "y" or "Y" or 0:
		from realsenseD435Class import realsenseD435Class
		RealSense_L = realsenseD435Class(EnvSetupVar.RS_SerialNumber_L)
		if select is 0:
			ARM_L.RealSense = RealSense_L
		print "Module \"RealsenseD435_L\" has been imported!"
	else:
		print "No realsense instance created."
elif EnvSetupVar.Need_RealSense_R:
	select = 0
	try:
		ARM_R
	except NameError:
		select = raw_input("WARNING!!! No PA10_ARM_R created! Are you sure continue to create realsense instance?[y/N]")

	if select is "y" or "Y" or 0:
		from realsenseD435Class import realsenseD435Class

		RealSense_R = realsenseD435Class(EnvSetupVar.RS_SerialNumber_R)
		if select is 0:
			ARM_R.RealSense = RealSense_R
		print "Module \"RealsenseD435_R\" has been imported!"
	else:
		print "No realsense instance created."
elif EnvSetupVar.Need_RealSense_BOTH:
	select_l = 0
	select_r = 0
	try:
		ARM_L
	except NameError:
		select_l = raw_input("WARNING!!! No PA10_ARM_L created! Are you sure continue to create realsense instance?[y/N]")
	try:
		ARM_R
	except NameError:
		select_r = raw_input("WARNING!!! No PA10_ARM_Right created! Are you sure continue to create realsense instance?[y/N]")

	if select_l is "y" or "Y" or 0:
		from realsenseD435Class import realsenseD435Class
		RealSense_L = realsenseD435Class(EnvSetupVar.RS_SerialNumber_L)
		if select_l is 0:
			ARM_L.RealSense = RealSense_L
		print "Module \"RealSense_L\" has been imported!"
	else:
		print "RealSense_L instance is not be created."

	if select_r is "y" or "Y" or 0:
		from realsenseD435Class import realsenseD435Class
		RealSense_R = realsenseD435Class(EnvSetupVar.RS_SerialNumber_R)
		if select_r is 0:
			ARM_R.RealSense = RealSense_R
		print "Module \"RealSense_R\" has been imported!"
	else:
		print "RealSense_R instance is not be created."
elif EnvSetupVar.Need_RealSense_OLD:
	from realsenseClass import realsenseClass
	realsense = realsenseClass()

if EnvSetupVar.Need_RealSense_L or EnvSetupVar.Need_RealSense_R or EnvSetupVar.Need_RealSense_BOTH:
	PointCloudProcess = realsenseD435Class.pcProcess.services["svPcProcess"].provided["sv_pp"].ref
	ImageProcess = realsenseD435Class.imProcess.services["svImProcess"].provided["sv_ip"].ref


# Gripper import
if EnvSetupVar.Need_Gripper_L:
	select = 0
	try:
		ARM_L
	except NameError:
		select = raw_input("WARNING!!! No PA10_ARM_L created! Are you sure continue to create gripper instance?[y/N]")

	if select is "y" or "Y" or 0:
		from share.tools.classes.parallelGripperClass import parallelGripperClass

		Gripper_L = parallelGripperClass("_l")
		Gripper_L.parallelGripper_free()
		if select is 0:
			ARM_L.Gripper = Gripper_L
		print "Module \"Gripper_L\" has been imported!"
	else:
		print "No gripper instance created."
elif EnvSetupVar.Need_Gripper_R:
	select = 0
	try:
		ARM_R
	except NameError:
		select = raw_input("WARNING!!! No PA10_ARM_R created! Are you sure continue to create gripper instance?[y/N]")
	if select is "y" or "Y" or 0:
		from share.tools.classes.parallelGripperClass import parallelGripperClass

		Gripper_R = parallelGripperClass("_r")
		Gripper_R.parallelGripper_free()
		if select is 0:
			ARM_R.Gripper = Gripper_R
		print "Module \"Gripper_R\" has been imported!"
	else:
		print "No gripper instance created."
elif EnvSetupVar.Need_Gripper_BOTH:
	select_l = 0
	select_r = 0
	try:
		ARM_L
	except NameError:
		select_l = raw_input("WARNING!!! No PA10_ARM_L created! Are you sure continue to create gripper instance?[y/N]")
	try:
		ARM_R
	except NameError:
		select_r = raw_input("WARNING!!! No PA10_ARM_R created! Are you sure continue to create gripper instance?[y/N]")

	if select_l is "y" or "Y" or 0:
		from share.tools.classes.parallelGripperClass import parallelGripperClass
		Gripper_L = parallelGripperClass("_l")
		Gripper_L.parallelGripper_free()
		if select_l is 0:
			ARM_L.Gripper = Gripper_L
		print "Module \"Gripper_L\" has been imported!"
	else:
		print "Gripper_L instance is not be created."

	if select_r is "y" or "Y" or 0:
		from share.tools.classes.parallelGripperClass import parallelGripperClass
		Gripper_R = parallelGripperClass("_r")
		Gripper_R.parallelGripper_free()
		if select_r is 0:
			ARM_R.Gripper = Gripper_R
		print "Module \"Gripper_R\" has been imported!"
	else:
		print "Gripper_R instance is not be created."
