# Python stubs generated by omniidl from sv_GetInfo.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "_GlobalIDL"
#
__name__ = "_GlobalIDL"
_0__GlobalIDL = omniORB.openModule("_GlobalIDL", r"sv_GetInfo.idl")
_0__GlobalIDL__POA = omniORB.openModule("_GlobalIDL__POA", r"sv_GetInfo.idl")

# #include "BasicDataType.idl"
import BasicDataType_idl
_0_RTC = omniORB.openModule("RTC")
_0_RTC__POA = omniORB.openModule("RTC__POA")
# #include "ExtendedDataTypes.idl"
import ExtendedDataTypes_idl
_0_RTC = omniORB.openModule("RTC")
_0_RTC__POA = omniORB.openModule("RTC__POA")
# #include "InterfaceDataTypes.idl"
import InterfaceDataTypes_idl
_0_RTC = omniORB.openModule("RTC")
_0_RTC__POA = omniORB.openModule("RTC__POA")

# interface GetInfoProcess
_0__GlobalIDL._d_GetInfoProcess = (omniORB.tcInternal.tv_objref, "IDL:GetInfoProcess:1.0", "GetInfoProcess")
omniORB.typeMapping["IDL:GetInfoProcess:1.0"] = _0__GlobalIDL._d_GetInfoProcess
_0__GlobalIDL.GetInfoProcess = omniORB.newEmptyClass()
class GetInfoProcess :
    _NP_RepositoryId = _0__GlobalIDL._d_GetInfoProcess[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil

    
    # typedef ... Matrix4_4
    class Matrix4_4:
        _NP_RepositoryId = "IDL:GetInfoProcess/Matrix4_4:1.0"
        def __init__(self, *args, **kw):
            raise RuntimeError("Cannot construct objects of this type.")
    _d_Matrix4_4  = (omniORB.tcInternal.tv_array, (omniORB.tcInternal.tv_array, omniORB.tcInternal.tv_double, 4), 4)
    _ad_Matrix4_4 = (omniORB.tcInternal.tv_alias, Matrix4_4._NP_RepositoryId, "Matrix4_4", (omniORB.tcInternal.tv_array, (omniORB.tcInternal.tv_array, omniORB.tcInternal.tv_double, 4), 4))
    _tc_Matrix4_4 = omniORB.tcInternal.createTypeCode(_ad_Matrix4_4)
    omniORB.registerType(Matrix4_4._NP_RepositoryId, _ad_Matrix4_4, _tc_Matrix4_4)


_0__GlobalIDL.GetInfoProcess = GetInfoProcess
_0__GlobalIDL._tc_GetInfoProcess = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_GetInfoProcess)
omniORB.registerType(GetInfoProcess._NP_RepositoryId, _0__GlobalIDL._d_GetInfoProcess, _0__GlobalIDL._tc_GetInfoProcess)

# GetInfoProcess operations and attributes
GetInfoProcess._d_GetCameraInfo = ((), ((omniORB.tcInternal.tv_string,0), ), None)
GetInfoProcess._d_Get_Color_IntrinsicParameters = ((), (omniORB.typeMapping["IDL:RTC/CameraInfo:1.0"], ), None)
GetInfoProcess._d_Get_LeftIR_IntrinsicParameters = ((), (omniORB.typeMapping["IDL:RTC/CameraInfo:1.0"], ), None)
GetInfoProcess._d_Get_RightIR_IntrinsicParameters = ((), (omniORB.typeMapping["IDL:RTC/CameraInfo:1.0"], ), None)
GetInfoProcess._d_Get_IR_RightToLeft_ExtrinsicParameters = ((), (omniORB.typeMapping["IDL:GetInfoProcess/Matrix4_4:1.0"], ), None)
GetInfoProcess._d_Get_Color_ToIRLeft_ExtrinsicParameters = ((), (omniORB.typeMapping["IDL:GetInfoProcess/Matrix4_4:1.0"], ), None)
GetInfoProcess._d_Get_IR_LeftToDepth_ExtrinsicParameters = ((), (omniORB.typeMapping["IDL:GetInfoProcess/Matrix4_4:1.0"], ), None)

# GetInfoProcess object reference
class _objref_GetInfoProcess (CORBA.Object):
    _NP_RepositoryId = GetInfoProcess._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def GetCameraInfo(self, *args):
        return _omnipy.invoke(self, "GetCameraInfo", _0__GlobalIDL.GetInfoProcess._d_GetCameraInfo, args)

    def Get_Color_IntrinsicParameters(self, *args):
        return _omnipy.invoke(self, "Get_Color_IntrinsicParameters", _0__GlobalIDL.GetInfoProcess._d_Get_Color_IntrinsicParameters, args)

    def Get_LeftIR_IntrinsicParameters(self, *args):
        return _omnipy.invoke(self, "Get_LeftIR_IntrinsicParameters", _0__GlobalIDL.GetInfoProcess._d_Get_LeftIR_IntrinsicParameters, args)

    def Get_RightIR_IntrinsicParameters(self, *args):
        return _omnipy.invoke(self, "Get_RightIR_IntrinsicParameters", _0__GlobalIDL.GetInfoProcess._d_Get_RightIR_IntrinsicParameters, args)

    def Get_IR_RightToLeft_ExtrinsicParameters(self, *args):
        return _omnipy.invoke(self, "Get_IR_RightToLeft_ExtrinsicParameters", _0__GlobalIDL.GetInfoProcess._d_Get_IR_RightToLeft_ExtrinsicParameters, args)

    def Get_Color_ToIRLeft_ExtrinsicParameters(self, *args):
        return _omnipy.invoke(self, "Get_Color_ToIRLeft_ExtrinsicParameters", _0__GlobalIDL.GetInfoProcess._d_Get_Color_ToIRLeft_ExtrinsicParameters, args)

    def Get_IR_LeftToDepth_ExtrinsicParameters(self, *args):
        return _omnipy.invoke(self, "Get_IR_LeftToDepth_ExtrinsicParameters", _0__GlobalIDL.GetInfoProcess._d_Get_IR_LeftToDepth_ExtrinsicParameters, args)

    __methods__ = ["GetCameraInfo", "Get_Color_IntrinsicParameters", "Get_LeftIR_IntrinsicParameters", "Get_RightIR_IntrinsicParameters", "Get_IR_RightToLeft_ExtrinsicParameters", "Get_Color_ToIRLeft_ExtrinsicParameters", "Get_IR_LeftToDepth_ExtrinsicParameters"] + CORBA.Object.__methods__

omniORB.registerObjref(GetInfoProcess._NP_RepositoryId, _objref_GetInfoProcess)
_0__GlobalIDL._objref_GetInfoProcess = _objref_GetInfoProcess
del GetInfoProcess, _objref_GetInfoProcess

# GetInfoProcess skeleton
__name__ = "_GlobalIDL__POA"
class GetInfoProcess (PortableServer.Servant):
    _NP_RepositoryId = _0__GlobalIDL.GetInfoProcess._NP_RepositoryId


    _omni_op_d = {"GetCameraInfo": _0__GlobalIDL.GetInfoProcess._d_GetCameraInfo, "Get_Color_IntrinsicParameters": _0__GlobalIDL.GetInfoProcess._d_Get_Color_IntrinsicParameters, "Get_LeftIR_IntrinsicParameters": _0__GlobalIDL.GetInfoProcess._d_Get_LeftIR_IntrinsicParameters, "Get_RightIR_IntrinsicParameters": _0__GlobalIDL.GetInfoProcess._d_Get_RightIR_IntrinsicParameters, "Get_IR_RightToLeft_ExtrinsicParameters": _0__GlobalIDL.GetInfoProcess._d_Get_IR_RightToLeft_ExtrinsicParameters, "Get_Color_ToIRLeft_ExtrinsicParameters": _0__GlobalIDL.GetInfoProcess._d_Get_Color_ToIRLeft_ExtrinsicParameters, "Get_IR_LeftToDepth_ExtrinsicParameters": _0__GlobalIDL.GetInfoProcess._d_Get_IR_LeftToDepth_ExtrinsicParameters}

GetInfoProcess._omni_skeleton = GetInfoProcess
_0__GlobalIDL__POA.GetInfoProcess = GetInfoProcess
omniORB.registerSkeleton(GetInfoProcess._NP_RepositoryId, GetInfoProcess)
del GetInfoProcess
__name__ = "_GlobalIDL"

# interface CameraControlProcess
_0__GlobalIDL._d_CameraControlProcess = (omniORB.tcInternal.tv_objref, "IDL:CameraControlProcess:1.0", "CameraControlProcess")
omniORB.typeMapping["IDL:CameraControlProcess:1.0"] = _0__GlobalIDL._d_CameraControlProcess
_0__GlobalIDL.CameraControlProcess = omniORB.newEmptyClass()
class CameraControlProcess :
    _NP_RepositoryId = _0__GlobalIDL._d_CameraControlProcess[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil

    
    # typedef ... CameraSetting
    class CameraSetting:
        _NP_RepositoryId = "IDL:CameraControlProcess/CameraSetting:1.0"
        def __init__(self, *args, **kw):
            raise RuntimeError("Cannot construct objects of this type.")
    _d_CameraSetting  = (omniORB.tcInternal.tv_array, omniORB.tcInternal.tv_long, 9)
    _ad_CameraSetting = (omniORB.tcInternal.tv_alias, CameraSetting._NP_RepositoryId, "CameraSetting", (omniORB.tcInternal.tv_array, omniORB.tcInternal.tv_long, 9))
    _tc_CameraSetting = omniORB.tcInternal.createTypeCode(_ad_CameraSetting)
    omniORB.registerType(CameraSetting._NP_RepositoryId, _ad_CameraSetting, _tc_CameraSetting)


_0__GlobalIDL.CameraControlProcess = CameraControlProcess
_0__GlobalIDL._tc_CameraControlProcess = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_CameraControlProcess)
omniORB.registerType(CameraControlProcess._NP_RepositoryId, _0__GlobalIDL._d_CameraControlProcess, _0__GlobalIDL._tc_CameraControlProcess)

# CameraControlProcess operations and attributes
CameraControlProcess._d_OpenCamera = (((omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_ulong), (omniORB.tcInternal.tv_boolean, ), None)
CameraControlProcess._d_OpenCameraWithSettings = (((omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_ulong, omniORB.typeMapping["IDL:CameraControlProcess/CameraSetting:1.0"]), (omniORB.tcInternal.tv_boolean, ), None)
CameraControlProcess._d_EnablePostProcess = ((omniORB.tcInternal.tv_boolean, ), (omniORB.tcInternal.tv_boolean, ), None)
CameraControlProcess._d_StartStream = ((), (), None)
CameraControlProcess._d_StopStream = ((), (), None)
CameraControlProcess._d_ImportAdvanceSettings = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)

# CameraControlProcess object reference
class _objref_CameraControlProcess (CORBA.Object):
    _NP_RepositoryId = CameraControlProcess._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def OpenCamera(self, *args):
        return _omnipy.invoke(self, "OpenCamera", _0__GlobalIDL.CameraControlProcess._d_OpenCamera, args)

    def OpenCameraWithSettings(self, *args):
        return _omnipy.invoke(self, "OpenCameraWithSettings", _0__GlobalIDL.CameraControlProcess._d_OpenCameraWithSettings, args)

    def EnablePostProcess(self, *args):
        return _omnipy.invoke(self, "EnablePostProcess", _0__GlobalIDL.CameraControlProcess._d_EnablePostProcess, args)

    def StartStream(self, *args):
        return _omnipy.invoke(self, "StartStream", _0__GlobalIDL.CameraControlProcess._d_StartStream, args)

    def StopStream(self, *args):
        return _omnipy.invoke(self, "StopStream", _0__GlobalIDL.CameraControlProcess._d_StopStream, args)

    def ImportAdvanceSettings(self, *args):
        return _omnipy.invoke(self, "ImportAdvanceSettings", _0__GlobalIDL.CameraControlProcess._d_ImportAdvanceSettings, args)

    __methods__ = ["OpenCamera", "OpenCameraWithSettings", "EnablePostProcess", "StartStream", "StopStream", "ImportAdvanceSettings"] + CORBA.Object.__methods__

omniORB.registerObjref(CameraControlProcess._NP_RepositoryId, _objref_CameraControlProcess)
_0__GlobalIDL._objref_CameraControlProcess = _objref_CameraControlProcess
del CameraControlProcess, _objref_CameraControlProcess

# CameraControlProcess skeleton
__name__ = "_GlobalIDL__POA"
class CameraControlProcess (PortableServer.Servant):
    _NP_RepositoryId = _0__GlobalIDL.CameraControlProcess._NP_RepositoryId


    _omni_op_d = {"OpenCamera": _0__GlobalIDL.CameraControlProcess._d_OpenCamera, "OpenCameraWithSettings": _0__GlobalIDL.CameraControlProcess._d_OpenCameraWithSettings, "EnablePostProcess": _0__GlobalIDL.CameraControlProcess._d_EnablePostProcess, "StartStream": _0__GlobalIDL.CameraControlProcess._d_StartStream, "StopStream": _0__GlobalIDL.CameraControlProcess._d_StopStream, "ImportAdvanceSettings": _0__GlobalIDL.CameraControlProcess._d_ImportAdvanceSettings}

CameraControlProcess._omni_skeleton = CameraControlProcess
_0__GlobalIDL__POA.CameraControlProcess = CameraControlProcess
omniORB.registerSkeleton(CameraControlProcess._NP_RepositoryId, CameraControlProcess)
del CameraControlProcess
__name__ = "_GlobalIDL"

#
# End of module "_GlobalIDL"
#
__name__ = "sv_GetInfo_idl"

_exported_modules = ( "_GlobalIDL", )

# The end.
