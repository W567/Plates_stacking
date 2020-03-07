// -*- C++ -*-
/*!
 * @file  RTC_ImageProcess.cpp
 * @brief RTC for image process
 * @date $Date$
 *
 * $Id$
 */

#include "RTC_ImageProcess.h"

// Module specification
// <rtc-template block="module_spec">
static const char* rtc_imageprocess_spec[] =
  {
    "implementation_id", "RTC_ImageProcess",
    "type_name",         "RTC_ImageProcess",
    "description",       "RTC for image process",
    "version",           "2.0.0",
    "vendor",            "Keisuke Nagano, Dong Chenyu",
    "category",          "Category",
    "activity_type",     "PERIODIC",
    "kind",              "DataFlowComponent",
    "max_instance",      "1",
    "language",          "C++",
    "lang_type",         "compile",
    ""
  };
// </rtc-template>

/*!
 * @brief constructor
 * @param manager Maneger Object
 */
RTC_ImageProcess::RTC_ImageProcess(RTC::Manager* manager)
    // <rtc-template block="initializer">
  : RTC::DataFlowComponentBase(manager),
    m_command_inIn("command_in", m_command_in),
    m_color_inIn("color_in", m_color_in),
    m_depth_inIn("depth_in", m_depth_in),
    m_ir_inIn("ir_in", m_ir_in),
    m_ir_right_inIn("ir_right_in", m_ir_right_in),
    m_color_in2In("color_in2", m_color_in2),
    m_depth_in2In("depth_in2", m_depth_in2),
    m_ir_in2In("ir_in2", m_ir_in2),
    m_ir_right_in2In("ir_right_in2", m_ir_right_in2),
    m_color_in3In("color_in3", m_color_in3),
    m_depth_in3In("depth_in3", m_depth_in3),
    m_ir_in3In("ir_in3", m_ir_in3),
    m_ir_right_in3In("ir_right_in3", m_ir_right_in3),
    m_color_in4In("color_in4", m_color_in4),
    m_depth_in4In("depth_in4", m_depth_in4),
    m_ir_in4In("ir_in4", m_ir_in4),
    m_ir_right_in4In("ir_right_in4", m_ir_right_in4),
    m_command_outOut("command_out", m_command_out),
    m_value_outOut("value_out", m_value_out),
    m_svImProcessPort("svImProcess"),
    m_sv_ip(
        &m_color_inIn,
        &m_color_in,
        &m_depth_inIn,
        &m_depth_in,
        &m_ir_inIn,
        &m_ir_in,
        &m_ir_right_inIn,
        &m_ir_right_in,

        &m_color_in2In,
        &m_color_in2,
        &m_depth_in2In,
        &m_depth_in2,
        &m_ir_in2In,
        &m_ir_in2,
        &m_ir_right_in2In,
        &m_ir_right_in2,

        &m_color_in3In,
        &m_color_in3,
        &m_depth_in3In,
        &m_depth_in3,
        &m_ir_in3In,
        &m_ir_in3,
        &m_ir_right_in3In,
        &m_ir_right_in3,

        &m_color_in4In,
        &m_color_in4,
        &m_depth_in4In,
        &m_depth_in4,
        &m_ir_in4In,
        &m_ir_in4,
        &m_ir_right_in4In,
        &m_ir_right_in4
    )

    // </rtc-template>
{
}

/*!
 * @brief destructor
 */
RTC_ImageProcess::~RTC_ImageProcess()
{
}



RTC::ReturnCode_t RTC_ImageProcess::onInitialize()
{
  // Registration: InPort/OutPort/Service
  // <rtc-template block="registration">
  // Set InPort buffers
  addInPort("command_in", m_command_inIn);
  addInPort("color_in", m_color_inIn);
  addInPort("depth_in", m_depth_inIn);
  addInPort("ir_in", m_ir_inIn);
  addInPort("ir_right_in", m_ir_right_inIn);
  addInPort("color_in2", m_color_in2In);
  addInPort("depth_in2", m_depth_in2In);
  addInPort("ir_in2", m_ir_in2In);
  addInPort("ir_right_in2", m_ir_right_in2In);
  addInPort("color_in3", m_color_in3In);
  addInPort("depth_in3", m_depth_in3In);
  addInPort("ir_in3", m_ir_in3In);
  addInPort("ir_right_in3", m_ir_right_in3In);
  addInPort("color_in4", m_color_in4In);
  addInPort("depth_in4", m_depth_in4In);
  addInPort("ir_in4", m_ir_in4In);
  addInPort("ir_right_in4", m_ir_right_in4In);
  
  // Set OutPort buffer
  addOutPort("command_out", m_command_outOut);
  addOutPort("value_out", m_value_outOut);
  
  // Set service provider to Ports
  m_svImProcessPort.registerProvider("sv_ip", "ComImProcess", m_sv_ip);
  
  // Set service consumers to Ports
  
  // Set CORBA Service Ports
  addPort(m_svImProcessPort);
  
  // </rtc-template>

  // <rtc-template block="bind_config">
  // </rtc-template>
  
  return RTC::RTC_OK;
}

/*
RTC::ReturnCode_t RTC_ImageProcess::onFinalize()
{
  return RTC::RTC_OK;
}
*/

/*
RTC::ReturnCode_t RTC_ImageProcess::onStartup(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}
*/

/*
RTC::ReturnCode_t RTC_ImageProcess::onShutdown(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}
*/


RTC::ReturnCode_t RTC_ImageProcess::onActivated(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}

/*
RTC::ReturnCode_t RTC_ImageProcess::onDeactivated(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}
*/


RTC::ReturnCode_t RTC_ImageProcess::onExecute(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}

/*
RTC::ReturnCode_t RTC_ImageProcess::onAborting(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}
*/


RTC::ReturnCode_t RTC_ImageProcess::onError(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}

/*
RTC::ReturnCode_t RTC_ImageProcess::onReset(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}
*/

/*
RTC::ReturnCode_t RTC_ImageProcess::onStateUpdate(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}
*/

/*
RTC::ReturnCode_t RTC_ImageProcess::onRateChanged(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}
*/



extern "C"
{
 
  void RTC_ImageProcessInit(RTC::Manager* manager)
  {
    coil::Properties profile(rtc_imageprocess_spec);
    manager->registerFactory(profile,
                             RTC::Create<RTC_ImageProcess>,
                             RTC::Delete<RTC_ImageProcess>);
  }
  
};


