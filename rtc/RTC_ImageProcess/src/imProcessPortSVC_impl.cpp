// -*-C++-*-
/*!
 * @file  imProcessPortSVC_impl.cpp
 * @brief Service implementation code of imProcessPort.idl
 *
 */

#include "imProcessPortSVC_impl.h"
#include "imProcessLib.h"

#include <omp.h>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/viz.hpp>

/*
 * Example implementational code for IDL interface ComImProcess
 */
ComImProcessSVC_impl::ComImProcessSVC_impl(
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
        RTC::CameraImage *m_ir_right4) {

    m_color_inIn		=	m_c_i;
    m_color_in			=	m_c;
    m_depth_inIn		=	m_d_i;
    m_depth_in			=	m_d;
    m_ir_in				=	m_ir;
    m_ir_inIn			=	m_ir_i;
    m_ir_right_in		=	m_ir_right;
    m_ir_right_inIn		=	m_ir_right_i;

    m_color2_inIn		=	m_c2_i;
    m_color2_in			=	m_c2;
    m_depth2_inIn		=	m_d2_i;
    m_depth2_in			=	m_d2;
    m_ir2_in			=	m_ir2;
    m_ir2_inIn			=	m_ir2_i;
    m_ir_right2_in		=	m_ir_right;
    m_ir_right2_inIn	=	m_ir_right_i;

    m_color3_inIn		=	m_c3_i;
    m_color3_in			=	m_c3;
    m_depth3_inIn		=	m_d3_i;
    m_depth3_in			=	m_d3;
    m_ir3_in			=	m_ir3;
    m_ir3_inIn			=	m_ir3_i;
    m_ir_right3_in		=	m_ir_right3;
    m_ir_right3_inIn	=	m_ir_right3_i;

    m_color4_inIn		=	m_c4_i;
    m_color4_in			=	m_c4;
    m_depth4_inIn		=	m_d4_i;
    m_depth4_in			=	m_d4;
    m_ir4_in			=	m_ir4;
    m_ir4_inIn			=	m_ir4_i;
    m_ir_right4_in		=	m_ir_right4;
    m_ir_right4_inIn	=	m_ir_right4_i;

    std::cout<<"RTC_ImageProcess initial over."<<std::endl;
}

ComImProcessSVC_impl::ComImProcessSVC_impl() {
    // Please add extra constructor code here.
}

ComImProcessSVC_impl::~ComImProcessSVC_impl() {
    // Please add extra destructor code here.
}

/*
 * Methods corresponding to IDL attributes and operations
 */

/*****************New Functions**************************/
/*
 * Methods corresponding to IDL attributes and operations
 */
ComImProcess::MultiImage_slice* ComImProcessSVC_impl::get_colorImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref)
{
    ComImProcess::MultiImage_slice* color = new RTC::CameraImage[4];

    std::cout << "exe get color image" << std::endl;
    if (m_color_inIn->isNew())
    {
        m_color_inIn->read();
        std::cout << "Channel1:discover new data" << std::endl;
        ref = true;
        (color[0]) = *m_color_in;
    }
    if (m_color2_inIn->isNew())
    {
        m_color2_inIn->read();
        std::cout << "Channel2:discover new data" << std::endl;
        ref = true;
        (color[1]) = *m_color2_in;
    }
    if (m_color3_inIn->isNew())
    {
        m_color3_inIn->read();
        std::cout << "Channel3:discover new data" << std::endl;
        ref = true;
        (color[2]) = *m_color3_in;
    }
    if (m_color4_inIn->isNew())
    {
        m_color4_inIn->read();
        std::cout << "Channel4:discover new data" << std::endl;
        ref = true;
        (color[3]) = *m_color4_in;
    }
    if(ref)
        return color;
    else
    {
        std::cout << "not discover new data" << std::endl;
        ref = false;
        return color;
    }
}

ComImProcess::MultiImage_slice* ComImProcessSVC_impl::get_irImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref)
{
    ComImProcess::MultiImage_slice* ir = new RTC::CameraImage[4];

    std::cout << "exe get ir image" << std::endl;
    if (m_ir_inIn->isNew())
    {
        m_ir_inIn->read();
        std::cout << "Channel1: discover new data" << std::endl;
        ref = true;
        ir[0] = *m_ir_in;
    }
    if (m_ir2_inIn->isNew())
    {
        m_ir2_inIn->read();
        std::cout << "Channel2: discover new data" << std::endl;
        ref = true;
        ir[1] = *m_ir2_in;
    }
    if (m_ir3_inIn->isNew())
    {
        m_ir3_inIn->read();
        std::cout << "Channel3: discover new data" << std::endl;
        ref = true;
        ir[2] = *m_ir3_in;
    }
    if (m_ir4_inIn->isNew())
    {
        m_ir4_inIn->read();
        std::cout << "Channel4: discover new data" << std::endl;
        ref = true;
        ir[3] = *m_ir4_in;
    }
    if(ref)
        return ir;
    else
    {
        std::cout << "not discover new data" << std::endl;
        ref = false;
        return ir;
    }
}

ComImProcess::MultiImage_slice* ComImProcessSVC_impl::get_ir_rightImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref)
{
    ComImProcess::MultiImage_slice* ir = new RTC::CameraImage[4];

    std::cout << "exe get ir_right image" << std::endl;
    if (m_ir_right_inIn->isNew())
    {
        m_ir_right_inIn->read();
        std::cout << "Channel1: discover new data" << std::endl;
        ref = true;
        ir[0] = *m_ir_right_in;
    }
    if (m_ir_right2_inIn->isNew())
    {
        m_ir_right2_inIn->read();
        std::cout << "Channel2: discover new data" << std::endl;
        ref = true;
        ir[1] = *m_ir_right2_in;
    }
    if (m_ir_right3_inIn->isNew())
    {
        m_ir_right3_inIn->read();
        std::cout << "Channel3: discover new data" << std::endl;
        ref = true;
        ir[2] = *m_ir_right3_in;
    }
    if (m_ir_right4_inIn->isNew())
    {
        m_ir_right4_inIn->read();
        std::cout << "Channel4: discover new data" << std::endl;
        ref = true;
        ir[3] = *m_ir_right4_in;
    }
    if(ref)
        return ir;
    else
    {
        std::cout << "not discover new data" << std::endl;
        ref = false;
        return ir;
    }
}

ComImProcess::MultiImage_slice* ComImProcessSVC_impl::get_depthImage(::CORBA::Short CameraBitMask, ::CORBA::Boolean& ref)
{
    ComImProcess::MultiImage_slice* depth = new RTC::CameraImage[4];

    std::cout << "exe get depth image" << std::endl;
    if (m_depth_inIn->isNew())
    {
        m_depth_inIn->read();
        std::cout << "Channel1: discover new data" << std::endl;
        ref = true;
        depth[0] = *m_depth_in;
    }
    if (m_depth2_inIn->isNew())
    {
        m_depth2_inIn->read();
        std::cout << "Channel2: discover new data" << std::endl;
        ref = true;
        depth[1] = *m_depth2_in;
    }
    if (m_depth3_inIn->isNew())
    {
        m_depth3_inIn->read();
        std::cout << "Channel3: discover new data" << std::endl;
        ref = true;
        depth[2] = *m_depth3_in;
    }
    if (m_depth4_inIn->isNew())
    {
        m_depth4_inIn->read();
        std::cout << "Channel4: discover new data" << std::endl;
        ref = true;
        depth[3] = *m_depth4_in;
    }
    if(ref)
        return depth;
    else
    {
        std::cout << "not discover new data" << std::endl;
        ref = false;
        return depth;
    }
}

static std::vector<std::string> StringSplit(const std::string &str, char sep)
{
	std::vector<std::string> v;
	std::stringstream ss(str);
	std::string buffer;
	while( std::getline(ss, buffer, sep) )
		v.push_back(buffer);
	return v;
}

/**
* @brief Combine the std::string that in std::vector, and seprated by [seprator]. \n
* @param[in] std::vector<std::string> src		Mask of which stream you want to setup and enable.
* @param[in] char seprator						Seprator. Default is none.
**/
static std::string StringCombine(std::vector<std::string> src, char seprator = '/')
{
	std::string res = "";
	for(std::string tmp : src)
		res += tmp + seprator;
	return res.erase(res.size()-1,1);
}

static std::string ProcessPathString(std::string src_path, std::string ChannelStr)
{
	char seprator = '/';

	auto path_list = StringSplit(src_path, seprator);
	std::string FileName = path_list[path_list.size() - 1];

	FileName.insert(0, ChannelStr);

	path_list[path_list.size() - 1] = FileName;
	return StringCombine(path_list, seprator);
}

::CORBA::Boolean ComImProcessSVC_impl::save_colorImage(::CORBA::Short CameraBitMask, const char* str)
{
    bool fSuccess = false;
    std::string Path(str);
    std::cout << "exe save color image" << std::endl;
    if (m_color_inIn->isNew() && ((CameraBitMask & 0x01) == 0x01))
    {
        m_color_inIn->read();
        std::cout << "Channel1: discover new data" << std::endl;

        cv::Mat color;
        cvt_RTCcolor_to_CVcolor(*m_color_in, color);

        cv::imwrite(ProcessPathString(Path, "Channel1_"), color);
        fSuccess = true;
    }
    if (m_color2_inIn->isNew() && ((CameraBitMask & 0x02) == 0x02))
    {
        m_color2_inIn->read();
        std::cout << "Channel2: discover new data" << std::endl;

        cv::Mat color;
        cvt_RTCcolor_to_CVcolor(*m_color2_in, color);

        cv::imwrite(ProcessPathString(Path, "Channel2_"), color);
        fSuccess = true;
    }
    if (m_color3_inIn->isNew() && ((CameraBitMask & 0x04) == 0x04))
    {
        m_color3_inIn->read();
        std::cout << "Channel3: discover new data" << std::endl;

        cv::Mat color;
        cvt_RTCcolor_to_CVcolor(*m_color3_in, color);

        cv::imwrite(ProcessPathString(Path, "Channel3_"), color);
        fSuccess = true;
    }
    if (m_color4_inIn->isNew() && ((CameraBitMask & 0x08) == 0x08))
    {
        m_color4_inIn->read();
        std::cout << "Channel4: discover new data" << std::endl;

        cv::Mat color;
        cvt_RTCcolor_to_CVcolor(*m_color4_in, color);

        cv::imwrite(ProcessPathString(Path, "Channel4_"), color);
        fSuccess = true;
    }
    if(fSuccess)
        return true;
    else
    {
        std::cout << "not discover new data" << std::endl;
        return false;
    }
}

::CORBA::Boolean ComImProcessSVC_impl::save_irImage(::CORBA::Short CameraBitMask, const char* str)
{
    bool fSuccess = false;
    std::string Path(str);
    std::cout << "exe save ir image" << std::endl;
    if (m_ir_inIn->isNew() && ((CameraBitMask & 0x01) == 0x01))
    {
        m_ir_inIn->read();
        std::cout << "Channel1: discover new data" << std::endl;

        cv::Mat ir;
        cvt_RTCcolor_to_CVcolor(*m_ir_in, ir);

        cv::imwrite(ProcessPathString(Path, "Channel1_"), ir);
        fSuccess = true;
    }
    if (m_ir2_inIn->isNew() && ((CameraBitMask & 0x02) == 0x02))
    {
        m_ir2_inIn->read();
        std::cout << "Channel2: discover new data" << std::endl;

        cv::Mat ir;
        cvt_RTCcolor_to_CVcolor(*m_ir2_in, ir);

        cv::imwrite(ProcessPathString(Path, "Channel2_"), ir);
        fSuccess = true;
    }
    if (m_ir3_inIn->isNew() && ((CameraBitMask & 0x04) == 0x04))
    {
        m_ir3_inIn->read();
        std::cout << "Channel3: discover new data" << std::endl;

        cv::Mat ir;
        cvt_RTCcolor_to_CVcolor(*m_ir3_in, ir);

        cv::imwrite(ProcessPathString(Path, "Channel3_"), ir);
        fSuccess = true;
    }
    if (m_ir4_inIn->isNew() && ((CameraBitMask & 0x08) == 0x08))
    {
        m_ir4_inIn->read();
        std::cout << "Channel4: discover new data" << std::endl;

        cv::Mat ir;
        cvt_RTCcolor_to_CVcolor(*m_ir4_in, ir);

        cv::imwrite(ProcessPathString(Path, "Channel4_"), ir);
        fSuccess = true;
    }
    if(fSuccess)
        return true;
    else
    {
        std::cout << "not discover new data" << std::endl;
        return false;
    }
}

::CORBA::Boolean ComImProcessSVC_impl::save_ir_rightImage(::CORBA::Short CameraBitMask, const char* str)
{
    bool fSuccess = false;
    std::string Path(str);
    std::cout << "exe save ir_right image" << std::endl;
    if (m_ir_right_inIn->isNew() && ((CameraBitMask & 0x01) == 0x01))
    {
        m_ir_right_inIn->read();
        std::cout << "Channel1: discover new data" << std::endl;

        cv::Mat ir;
        cvt_RTCcolor_to_CVcolor(*m_ir_right_in, ir);

        cv::imwrite(ProcessPathString(Path, "Channel1_"), ir);
        fSuccess = true;
    }
    if (m_ir_right2_inIn->isNew() && ((CameraBitMask & 0x02) == 0x02))
    {
        m_ir_right2_inIn->read();
        std::cout << "Channel2: discover new data" << std::endl;

        cv::Mat ir;
        cvt_RTCcolor_to_CVcolor(*m_ir_right2_in, ir);

        cv::imwrite(ProcessPathString(Path, "Channel2_"), ir);
        fSuccess = true;
    }
    if (m_ir_right3_inIn->isNew() && ((CameraBitMask & 0x04) == 0x04))
    {
        m_ir_right3_inIn->read();
        std::cout << "Channel3: discover new data" << std::endl;

        cv::Mat ir;
        cvt_RTCcolor_to_CVcolor(*m_ir_right3_in, ir);

        cv::imwrite(ProcessPathString(Path, "Channel3_"), ir);
        fSuccess = true;
    }
    if (m_ir_right4_inIn->isNew() && ((CameraBitMask & 0x08) == 0x08))
    {
        m_ir_right4_inIn->read();
        std::cout << "Channel4: discover new data" << std::endl;

        cv::Mat ir;
        cvt_RTCcolor_to_CVcolor(*m_ir_right4_in, ir);

        cv::imwrite(ProcessPathString(Path, "Channel4_"), ir);
        fSuccess = true;
    }
    if(fSuccess)
        return true;
    else
    {
        std::cout << "not discover new data" << std::endl;
        return false;
    }
}

::CORBA::Boolean ComImProcessSVC_impl::save_depthImage(::CORBA::Short CameraBitMask, const char* str)
{
    bool fSuccess = false;
    std::string Path(str);
    std::cout << "exe save depth image" << std::endl;
    if (m_depth_inIn->isNew() && ((CameraBitMask & 0x01) == 0x01))
    {
        m_depth_inIn->read();
        std::cout << "Channel1: discover new data" << std::endl;

        cv::Mat depth;
        cvt_RTCcolor_to_CVcolor(*m_depth_in, depth);

        cv::imwrite(ProcessPathString(Path, "Channel1_"), depth);
        fSuccess = true;
    }
    if (m_depth2_inIn->isNew() && ((CameraBitMask & 0x02) == 0x02))
    {
        m_depth2_inIn->read();
        std::cout << "Channel2: discover new data" << std::endl;

        cv::Mat depth;
        cvt_RTCcolor_to_CVcolor(*m_depth2_in, depth);

        cv::imwrite(ProcessPathString(Path, "Channel2_"), depth);
        fSuccess = true;
    }
    if (m_depth3_inIn->isNew() && ((CameraBitMask & 0x04) == 0x04))
    {
        m_depth3_inIn->read();
        std::cout << "Channel3: discover new data" << std::endl;

        cv::Mat depth;
        cvt_RTCcolor_to_CVcolor(*m_depth3_in, depth);

        cv::imwrite(ProcessPathString(Path, "Channel3_"), depth);
        fSuccess = true;
    }
    if (m_depth4_inIn->isNew() && ((CameraBitMask & 0x08) == 0x08))
    {
        m_depth4_inIn->read();
        std::cout << "Channel4: discover new data" << std::endl;

        cv::Mat depth;
        cvt_RTCcolor_to_CVcolor(*m_depth4_in, depth);

        cv::imwrite(ProcessPathString(Path, "Channel4_"), depth);
        fSuccess = true;
    }
    if(fSuccess)
        return true;
    else
    {
        std::cout << "not discover new data" << std::endl;
        return false;
    }
}
