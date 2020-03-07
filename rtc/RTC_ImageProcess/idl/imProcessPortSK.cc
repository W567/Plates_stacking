// This file is generated by omniidl (C++ backend)- omniORB_4_1. Do not edit.

#include "imProcessPort.hh"
#include <omniORB4/IOP_S.h>
#include <omniORB4/IOP_C.h>
#include <omniORB4/callDescriptor.h>
#include <omniORB4/callHandle.h>
#include <omniORB4/objTracker.h>


OMNI_USING_NAMESPACE(omni)

static const char* _0RL_library_version = omniORB_4_1;



ComImProcess_ptr ComImProcess_Helper::_nil() {
  return ::ComImProcess::_nil();
}

::CORBA::Boolean ComImProcess_Helper::is_nil(::ComImProcess_ptr p) {
  return ::CORBA::is_nil(p);

}

void ComImProcess_Helper::release(::ComImProcess_ptr p) {
  ::CORBA::release(p);
}

void ComImProcess_Helper::marshalObjRef(::ComImProcess_ptr obj, cdrStream& s) {
  ::ComImProcess::_marshalObjRef(obj, s);
}

ComImProcess_ptr ComImProcess_Helper::unmarshalObjRef(cdrStream& s) {
  return ::ComImProcess::_unmarshalObjRef(s);
}

void ComImProcess_Helper::duplicate(::ComImProcess_ptr obj) {
  if( obj && !obj->_NP_is_nil() )  omni::duplicateObjRef(obj);
}

ComImProcess_ptr
ComImProcess::_duplicate(::ComImProcess_ptr obj)
{
  if( obj && !obj->_NP_is_nil() )  omni::duplicateObjRef(obj);
  return obj;
}

ComImProcess_ptr
ComImProcess::_narrow(::CORBA::Object_ptr obj)
{
  if( !obj || obj->_NP_is_nil() || obj->_NP_is_pseudo() ) return _nil();
  _ptr_type e = (_ptr_type) obj->_PR_getobj()->_realNarrow(_PD_repoId);
  return e ? e : _nil();
}


ComImProcess_ptr
ComImProcess::_unchecked_narrow(::CORBA::Object_ptr obj)
{
  if( !obj || obj->_NP_is_nil() || obj->_NP_is_pseudo() ) return _nil();
  _ptr_type e = (_ptr_type) obj->_PR_getobj()->_uncheckedNarrow(_PD_repoId);
  return e ? e : _nil();
}

ComImProcess_ptr
ComImProcess::_nil()
{
#ifdef OMNI_UNLOADABLE_STUBS
  static _objref_ComImProcess _the_nil_obj;
  return &_the_nil_obj;
#else
  static _objref_ComImProcess* _the_nil_ptr = 0;
  if( !_the_nil_ptr ) {
    omni::nilRefLock().lock();
    if( !_the_nil_ptr ) {
      _the_nil_ptr = new _objref_ComImProcess;
      registerNilCorbaObject(_the_nil_ptr);
    }
    omni::nilRefLock().unlock();
  }
  return _the_nil_ptr;
#endif
}

const char* ComImProcess::_PD_repoId = "IDL:ComImProcess:1.0";


_objref_ComImProcess::~_objref_ComImProcess() {
  
}


_objref_ComImProcess::_objref_ComImProcess(omniIOR* ior, omniIdentity* id) :
   omniObjRef(::ComImProcess::_PD_repoId, ior, id, 1)
   
   
{
  _PR_setobj(this);
}

void*
_objref_ComImProcess::_ptrToObjRef(const char* id)
{
  if( id == ::ComImProcess::_PD_repoId )
    return (::ComImProcess_ptr) this;
  
  if( id == ::CORBA::Object::_PD_repoId )
    return (::CORBA::Object_ptr) this;

  if( omni::strMatch(id, ::ComImProcess::_PD_repoId) )
    return (::ComImProcess_ptr) this;
  
  if( omni::strMatch(id, ::CORBA::Object::_PD_repoId) )
    return (::CORBA::Object_ptr) this;

  return 0;
}

// Proxy call descriptor class. Mangled signature:
//  _a4_cRTC_mCameraImage_i_cshort_o_cboolean
class _0RL_cd_aa9826de59cbd897_00000000
  : public omniCallDescriptor
{
public:
  inline _0RL_cd_aa9826de59cbd897_00000000(LocalCallFn lcfn,const char* op_,size_t oplen,_CORBA_Boolean upcall=0):
     omniCallDescriptor(lcfn, op_, oplen, 0, _user_exns, 0, upcall)
  {
    
  }
  
  void marshalArguments(cdrStream&);
  void unmarshalArguments(cdrStream&);

  void unmarshalReturnedValues(cdrStream&);
  void marshalReturnedValues(cdrStream&);
  
  
  static const char* const _user_exns[];

  ::CORBA::Short arg_0;
  ::CORBA::Boolean arg_1;
  ComImProcess::MultiImage_var result;
};

void _0RL_cd_aa9826de59cbd897_00000000::marshalArguments(cdrStream& _n)
{
  arg_0 >>= _n;

}

void _0RL_cd_aa9826de59cbd897_00000000::unmarshalArguments(cdrStream& _n)
{
  (::CORBA::Short&)arg_0 <<= _n;

}

void _0RL_cd_aa9826de59cbd897_00000000::marshalReturnedValues(cdrStream& _n)
{
  {
    for (_CORBA_ULong _0i0 = 0; _0i0 < 4; _0i0++){
      (const RTC::CameraImage&) result[_0i0] >>= _n;
    }
  }
  _n.marshalBoolean(arg_1);

}

void _0RL_cd_aa9826de59cbd897_00000000::unmarshalReturnedValues(cdrStream& _n)
{
  result = ComImProcess::MultiImage_alloc();
  {
    for (_CORBA_ULong _0i0 = 0; _0i0 < 4; _0i0++){
      (RTC::CameraImage&)result[_0i0] <<= _n;
    }
  }
  arg_1 = _n.unmarshalBoolean();

}

const char* const _0RL_cd_aa9826de59cbd897_00000000::_user_exns[] = {
  0
};

// Local call call-back function.
static void
_0RL_lcfn_aa9826de59cbd897_10000000(omniCallDescriptor* cd, omniServant* svnt)
{
  _0RL_cd_aa9826de59cbd897_00000000* tcd = (_0RL_cd_aa9826de59cbd897_00000000*)cd;
  _impl_ComImProcess* impl = (_impl_ComImProcess*) svnt->_ptrToInterface(ComImProcess::_PD_repoId);
  tcd->result = impl->get_colorImage(tcd->arg_0, tcd->arg_1);


}

ComImProcess::MultiImage_slice* _objref_ComImProcess::get_colorImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref)
{
  _0RL_cd_aa9826de59cbd897_00000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_10000000, "get_colorImage", 15);
  _call_desc.arg_0 = CameraBitMask;

  _invoke(_call_desc);
  ref = _call_desc.arg_1;
  return _call_desc.result._retn();


}
// Local call call-back function.
static void
_0RL_lcfn_aa9826de59cbd897_20000000(omniCallDescriptor* cd, omniServant* svnt)
{
  _0RL_cd_aa9826de59cbd897_00000000* tcd = (_0RL_cd_aa9826de59cbd897_00000000*)cd;
  _impl_ComImProcess* impl = (_impl_ComImProcess*) svnt->_ptrToInterface(ComImProcess::_PD_repoId);
  tcd->result = impl->get_irImage(tcd->arg_0, tcd->arg_1);


}

ComImProcess::MultiImage_slice* _objref_ComImProcess::get_irImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref)
{
  _0RL_cd_aa9826de59cbd897_00000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_20000000, "get_irImage", 12);
  _call_desc.arg_0 = CameraBitMask;

  _invoke(_call_desc);
  ref = _call_desc.arg_1;
  return _call_desc.result._retn();


}
// Local call call-back function.
static void
_0RL_lcfn_aa9826de59cbd897_30000000(omniCallDescriptor* cd, omniServant* svnt)
{
  _0RL_cd_aa9826de59cbd897_00000000* tcd = (_0RL_cd_aa9826de59cbd897_00000000*)cd;
  _impl_ComImProcess* impl = (_impl_ComImProcess*) svnt->_ptrToInterface(ComImProcess::_PD_repoId);
  tcd->result = impl->get_ir_rightImage(tcd->arg_0, tcd->arg_1);


}

ComImProcess::MultiImage_slice* _objref_ComImProcess::get_ir_rightImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref)
{
  _0RL_cd_aa9826de59cbd897_00000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_30000000, "get_ir_rightImage", 18);
  _call_desc.arg_0 = CameraBitMask;

  _invoke(_call_desc);
  ref = _call_desc.arg_1;
  return _call_desc.result._retn();


}
// Local call call-back function.
static void
_0RL_lcfn_aa9826de59cbd897_40000000(omniCallDescriptor* cd, omniServant* svnt)
{
  _0RL_cd_aa9826de59cbd897_00000000* tcd = (_0RL_cd_aa9826de59cbd897_00000000*)cd;
  _impl_ComImProcess* impl = (_impl_ComImProcess*) svnt->_ptrToInterface(ComImProcess::_PD_repoId);
  tcd->result = impl->get_depthImage(tcd->arg_0, tcd->arg_1);


}

ComImProcess::MultiImage_slice* _objref_ComImProcess::get_depthImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref)
{
  _0RL_cd_aa9826de59cbd897_00000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_40000000, "get_depthImage", 15);
  _call_desc.arg_0 = CameraBitMask;

  _invoke(_call_desc);
  ref = _call_desc.arg_1;
  return _call_desc.result._retn();


}
// Proxy call descriptor class. Mangled signature:
//  _cboolean_i_cshort_i_cstring
class _0RL_cd_aa9826de59cbd897_50000000
  : public omniCallDescriptor
{
public:
  inline _0RL_cd_aa9826de59cbd897_50000000(LocalCallFn lcfn,const char* op_,size_t oplen,_CORBA_Boolean upcall=0):
     omniCallDescriptor(lcfn, op_, oplen, 0, _user_exns, 0, upcall)
  {
    
  }
  
  void marshalArguments(cdrStream&);
  void unmarshalArguments(cdrStream&);

  void unmarshalReturnedValues(cdrStream&);
  void marshalReturnedValues(cdrStream&);
  
  
  static const char* const _user_exns[];

  ::CORBA::Short arg_0;
  ::CORBA::String_var arg_1_;
  const char* arg_1;
  ::CORBA::Boolean result;
};

void _0RL_cd_aa9826de59cbd897_50000000::marshalArguments(cdrStream& _n)
{
  arg_0 >>= _n;
  _n.marshalString(arg_1,0);

}

void _0RL_cd_aa9826de59cbd897_50000000::unmarshalArguments(cdrStream& _n)
{
  (::CORBA::Short&)arg_0 <<= _n;
  arg_1_ = _n.unmarshalString(0);
  arg_1 = arg_1_.in();

}

void _0RL_cd_aa9826de59cbd897_50000000::marshalReturnedValues(cdrStream& _n)
{
  _n.marshalBoolean(result);

}

void _0RL_cd_aa9826de59cbd897_50000000::unmarshalReturnedValues(cdrStream& _n)
{
  result = _n.unmarshalBoolean();

}

const char* const _0RL_cd_aa9826de59cbd897_50000000::_user_exns[] = {
  0
};

// Local call call-back function.
static void
_0RL_lcfn_aa9826de59cbd897_60000000(omniCallDescriptor* cd, omniServant* svnt)
{
  _0RL_cd_aa9826de59cbd897_50000000* tcd = (_0RL_cd_aa9826de59cbd897_50000000*)cd;
  _impl_ComImProcess* impl = (_impl_ComImProcess*) svnt->_ptrToInterface(ComImProcess::_PD_repoId);
  tcd->result = impl->save_colorImage(tcd->arg_0, tcd->arg_1);


}

::CORBA::Boolean _objref_ComImProcess::save_colorImage(::CORBA::Short CameraBitMask, const char* str)
{
  _0RL_cd_aa9826de59cbd897_50000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_60000000, "save_colorImage", 16);
  _call_desc.arg_0 = CameraBitMask;
  _call_desc.arg_1 = str;

  _invoke(_call_desc);
  return _call_desc.result;


}
// Local call call-back function.
static void
_0RL_lcfn_aa9826de59cbd897_70000000(omniCallDescriptor* cd, omniServant* svnt)
{
  _0RL_cd_aa9826de59cbd897_50000000* tcd = (_0RL_cd_aa9826de59cbd897_50000000*)cd;
  _impl_ComImProcess* impl = (_impl_ComImProcess*) svnt->_ptrToInterface(ComImProcess::_PD_repoId);
  tcd->result = impl->save_irImage(tcd->arg_0, tcd->arg_1);


}

::CORBA::Boolean _objref_ComImProcess::save_irImage(::CORBA::Short CameraBitMask, const char* str)
{
  _0RL_cd_aa9826de59cbd897_50000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_70000000, "save_irImage", 13);
  _call_desc.arg_0 = CameraBitMask;
  _call_desc.arg_1 = str;

  _invoke(_call_desc);
  return _call_desc.result;


}
// Local call call-back function.
static void
_0RL_lcfn_aa9826de59cbd897_80000000(omniCallDescriptor* cd, omniServant* svnt)
{
  _0RL_cd_aa9826de59cbd897_50000000* tcd = (_0RL_cd_aa9826de59cbd897_50000000*)cd;
  _impl_ComImProcess* impl = (_impl_ComImProcess*) svnt->_ptrToInterface(ComImProcess::_PD_repoId);
  tcd->result = impl->save_ir_rightImage(tcd->arg_0, tcd->arg_1);


}

::CORBA::Boolean _objref_ComImProcess::save_ir_rightImage(::CORBA::Short CameraBitMask, const char* str)
{
  _0RL_cd_aa9826de59cbd897_50000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_80000000, "save_ir_rightImage", 19);
  _call_desc.arg_0 = CameraBitMask;
  _call_desc.arg_1 = str;

  _invoke(_call_desc);
  return _call_desc.result;


}
// Local call call-back function.
static void
_0RL_lcfn_aa9826de59cbd897_90000000(omniCallDescriptor* cd, omniServant* svnt)
{
  _0RL_cd_aa9826de59cbd897_50000000* tcd = (_0RL_cd_aa9826de59cbd897_50000000*)cd;
  _impl_ComImProcess* impl = (_impl_ComImProcess*) svnt->_ptrToInterface(ComImProcess::_PD_repoId);
  tcd->result = impl->save_depthImage(tcd->arg_0, tcd->arg_1);


}

::CORBA::Boolean _objref_ComImProcess::save_depthImage(::CORBA::Short CameraBitMask, const char* str)
{
  _0RL_cd_aa9826de59cbd897_50000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_90000000, "save_depthImage", 16);
  _call_desc.arg_0 = CameraBitMask;
  _call_desc.arg_1 = str;

  _invoke(_call_desc);
  return _call_desc.result;


}
_pof_ComImProcess::~_pof_ComImProcess() {}


omniObjRef*
_pof_ComImProcess::newObjRef(omniIOR* ior, omniIdentity* id)
{
  return new ::_objref_ComImProcess(ior, id);
}


::CORBA::Boolean
_pof_ComImProcess::is_a(const char* id) const
{
  if( omni::ptrStrMatch(id, ::ComImProcess::_PD_repoId) )
    return 1;
  
  return 0;
}

const _pof_ComImProcess _the_pof_ComImProcess;

_impl_ComImProcess::~_impl_ComImProcess() {}


::CORBA::Boolean
_impl_ComImProcess::_dispatch(omniCallHandle& _handle)
{
  const char* op = _handle.operation_name();

  if( omni::strMatch(op, "get_colorImage") ) {

    _0RL_cd_aa9826de59cbd897_00000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_10000000, "get_colorImage", 15, 1);
    
    _handle.upcall(this,_call_desc);
    return 1;
  }

  if( omni::strMatch(op, "get_irImage") ) {

    _0RL_cd_aa9826de59cbd897_00000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_20000000, "get_irImage", 12, 1);
    
    _handle.upcall(this,_call_desc);
    return 1;
  }

  if( omni::strMatch(op, "get_ir_rightImage") ) {

    _0RL_cd_aa9826de59cbd897_00000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_30000000, "get_ir_rightImage", 18, 1);
    
    _handle.upcall(this,_call_desc);
    return 1;
  }

  if( omni::strMatch(op, "get_depthImage") ) {

    _0RL_cd_aa9826de59cbd897_00000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_40000000, "get_depthImage", 15, 1);
    
    _handle.upcall(this,_call_desc);
    return 1;
  }

  if( omni::strMatch(op, "save_colorImage") ) {

    _0RL_cd_aa9826de59cbd897_50000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_60000000, "save_colorImage", 16, 1);
    
    _handle.upcall(this,_call_desc);
    return 1;
  }

  if( omni::strMatch(op, "save_irImage") ) {

    _0RL_cd_aa9826de59cbd897_50000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_70000000, "save_irImage", 13, 1);
    
    _handle.upcall(this,_call_desc);
    return 1;
  }

  if( omni::strMatch(op, "save_ir_rightImage") ) {

    _0RL_cd_aa9826de59cbd897_50000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_80000000, "save_ir_rightImage", 19, 1);
    
    _handle.upcall(this,_call_desc);
    return 1;
  }

  if( omni::strMatch(op, "save_depthImage") ) {

    _0RL_cd_aa9826de59cbd897_50000000 _call_desc(_0RL_lcfn_aa9826de59cbd897_90000000, "save_depthImage", 16, 1);
    
    _handle.upcall(this,_call_desc);
    return 1;
  }


  return 0;
}

void*
_impl_ComImProcess::_ptrToInterface(const char* id)
{
  if( id == ::ComImProcess::_PD_repoId )
    return (::_impl_ComImProcess*) this;
  
  if( id == ::CORBA::Object::_PD_repoId )
    return (void*) 1;

  if( omni::strMatch(id, ::ComImProcess::_PD_repoId) )
    return (::_impl_ComImProcess*) this;
  
  if( omni::strMatch(id, ::CORBA::Object::_PD_repoId) )
    return (void*) 1;
  return 0;
}

const char*
_impl_ComImProcess::_mostDerivedRepoId()
{
  return ::ComImProcess::_PD_repoId;
}

POA_ComImProcess::~POA_ComImProcess() {}
