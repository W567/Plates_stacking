// -*- C++ -*-
/*!
 *
 * THIS FILE IS GENERATED AUTOMATICALLY!! DO NOT EDIT!!
 *
 * @file pcProcessPortSkel.cpp 
 * @brief pcProcessPort server skeleton wrapper
 * @date Mon Jun  4 20:28:18 2018 
 *
 */

#include "pcProcessPortSkel.h"

#if defined ORB_IS_TAO
#  include "pcProcessPortC.cpp"
#  include "pcProcessPortS.cpp"
#elif defined ORB_IS_OMNIORB
#  include "pcProcessPortSK.cc"
#  include "pcProcessPortDynSK.cc"
#elif defined ORB_IS_MICO
#  include "pcProcessPort.cc"
#  include "pcProcessPort_skel.cc"
#elif defined ORB_IS_ORBIT2
#  include "pcProcessPort-cpp-stubs.cc"
#  include "pcProcessPort-cpp-skels.cc"
#elif defined ORB_IS_RTORB
#  include "OpenRTM-aist-decls.h"
#  include "pcProcessPort-common.c"
#  include "pcProcessPort-stubs.c"
#  include "pcProcessPort-skels.c"
#  include "pcProcessPort-skelimpl.c"
#else
#  error "NO ORB defined"
#endif

// end of pcProcessPortSkel.cpp
