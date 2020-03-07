// -*-C++-*-
/*!
 * @file  imProcessPortSVC_impl.h
 * @brief Service implementation header of imProcessPort.idl
 *
 */

#include "InterfaceDataTypesSkel.h"
#include "BasicDataTypeSkel.h"
#include "ExtendedDataTypesSkel.h"

#include "imProcessPortSkel.h"

#include <rtm/DataInPort.h>
#include <rtm/DataOutPort.h>

//
#include <opencv2/opencv.hpp>

#ifndef IMPROCESSPORTSVC_IMPL_H
#define IMPROCESSPORTSVC_IMPL_H

/*!
 * @class ComImProcessSVC_impl
 * Example class implementing IDL interface ComImProcess
 */
class ComImProcessSVC_impl: public virtual POA_ComImProcess,
        public virtual PortableServer::RefCountServantBase {
private:
    // Make sure all instances are built on the heap by making the
    // destructor non-public
    //virtual ~ComImProcessSVC_impl();

public:
    /*!
     * @brief standard constructor
     */
    ComImProcessSVC_impl(
            RTC::InPort<RTC::CameraImage> *m_c_i,
            RTC::CameraImage *m_c,
            RTC::InPort<RTC::CameraImage> *m_d_i,
            RTC::CameraImage *m_d,
            RTC::InPort<RTC::CameraImage> *m_ir_i,
            RTC::CameraImage *m_ir,
            RTC::InPort<RTC::CameraImage> *m_ir_right_i,
            RTC::CameraImage *m_ir_right,

            RTC::InPort<RTC::CameraImage> *m_c2_i,
            RTC::CameraImage *m_c2,
            RTC::InPort<RTC::CameraImage> *m_d2_i,
            RTC::CameraImage *m_d2,
            RTC::InPort<RTC::CameraImage> *m_ir2_i,
            RTC::CameraImage *m_ir2,
            RTC::InPort<RTC::CameraImage> *m_ir_right2_i,
            RTC::CameraImage *m_ir_right2,

            RTC::InPort<RTC::CameraImage> *m_c3_i,
            RTC::CameraImage *m_c3,
            RTC::InPort<RTC::CameraImage> *m_d3_i,
            RTC::CameraImage *m_d3,
            RTC::InPort<RTC::CameraImage> *m_ir3_i,
            RTC::CameraImage *m_ir3,
            RTC::InPort<RTC::CameraImage> *m_ir_right3_i,
            RTC::CameraImage *m_ir_right3,

            RTC::InPort<RTC::CameraImage> *m_c4_i,
            RTC::CameraImage *m_c4,
            RTC::InPort<RTC::CameraImage> *m_d4_i,
            RTC::CameraImage *m_d4,
            RTC::InPort<RTC::CameraImage> *m_ir4_i,
            RTC::CameraImage *m_ir4,
            RTC::InPort<RTC::CameraImage> *m_ir_right4_i,
            RTC::CameraImage *m_ir_right4);
    ComImProcessSVC_impl();
    /*!
     * @brief destructor
     */
    virtual ~ComImProcessSVC_impl();

    // attributes and operations
    ComImProcess::MultiImage_slice* get_colorImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref);
    ComImProcess::MultiImage_slice* get_irImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref);
    ComImProcess::MultiImage_slice* get_ir_rightImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref);
    ComImProcess::MultiImage_slice* get_depthImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref);
    ::CORBA::Boolean save_colorImage(::CORBA::Short CameraBitMask, const char* str);
    ::CORBA::Boolean save_irImage(::CORBA::Short CameraBitMask, const char* str);
    ::CORBA::Boolean save_ir_rightImage(::CORBA::Short CameraBitMask, const char* str);
    ::CORBA::Boolean save_depthImage(::CORBA::Short CameraBitMask, const char* str);


    //User Variable


    //User Function


    // ------------------ argument -----------------------------
    RTC::InPort<RTC::CameraImage> *m_color_inIn;
    RTC::CameraImage *m_color_in;
    RTC::InPort<RTC::CameraImage> *m_depth_inIn;
    RTC::CameraImage *m_depth_in;
    RTC::InPort<RTC::CameraImage> *m_ir_inIn;
    RTC::CameraImage *m_ir_in;
    RTC::InPort<RTC::CameraImage> *m_ir_right_inIn;
    RTC::CameraImage *m_ir_right_in;

    RTC::InPort<RTC::CameraImage> *m_color2_inIn;
    RTC::CameraImage *m_color2_in;
    RTC::InPort<RTC::CameraImage> *m_depth2_inIn;
    RTC::CameraImage *m_depth2_in;
    RTC::InPort<RTC::CameraImage> *m_ir2_inIn;
    RTC::CameraImage *m_ir2_in;
    RTC::InPort<RTC::CameraImage> *m_ir_right2_inIn;
    RTC::CameraImage *m_ir_right2_in;

    RTC::InPort<RTC::CameraImage> *m_color3_inIn;
    RTC::CameraImage *m_color3_in;
    RTC::InPort<RTC::CameraImage> *m_depth3_inIn;
    RTC::CameraImage *m_depth3_in;
    RTC::InPort<RTC::CameraImage> *m_ir3_inIn;
    RTC::CameraImage *m_ir3_in;
    RTC::InPort<RTC::CameraImage> *m_ir_right3_inIn;
    RTC::CameraImage *m_ir_right3_in;

    RTC::InPort<RTC::CameraImage> *m_color4_inIn;
    RTC::CameraImage *m_color4_in;
    RTC::InPort<RTC::CameraImage> *m_depth4_inIn;
    RTC::CameraImage *m_depth4_in;
    RTC::InPort<RTC::CameraImage> *m_ir4_inIn;
    RTC::CameraImage *m_ir4_in;
    RTC::InPort<RTC::CameraImage> *m_ir_right4_inIn;
    RTC::CameraImage *m_ir_right4_in;

};

#endif // IMPROCESSPORTSVC_IMPL_H
