/*
 * imProcessLib.cpp
 *
 *  Created on: 2017/05/25
 *      Author: cook
 */

// ======================================================================
//
//	include
//
// =======================================================================
#include "imProcessLib.h"
#include <time.h>
#include <random>
#include <vector>
#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/opencv.hpp>

using namespace cv;
// ======================================================================
//
//	program
//
// =======================================================================

void cvt_RTCcolor_to_CVcolor(RTC::CameraImage& rtc_color, cv::Mat& color) {

	// ========== color convert RTC -> opencv ==============
	//////// In our environment, "bpp" is means "Bytes per pixel".
	int len = rtc_color.width * rtc_color.height * rtc_color.bpp;
	cv::Size imageSize = cv::Size(rtc_color.width, rtc_color.height);
	std::string tmp(rtc_color.format);
//	std::cout << tmp << std::endl;

	if(tmp == "RGB8" || tmp == "BGR8")
		color = cv::Mat(imageSize, CV_8UC3);
	else if(tmp == "RGBA8" || tmp == "BGRA8")
		color = cv::Mat(imageSize, CV_8UC4);
	else if(tmp == "Y8")
		color = cv::Mat(imageSize, CV_8UC1);
	else if(tmp == "Y16" || tmp == "Z16")
		color = cv::Mat(imageSize, CV_16UC1);

	memcpy(color.data, (void*) &(rtc_color.pixels[0]), len);

}

void cvt_RTCdepth_to_CVdepth(RTC::CameraImage& rtc_depth, cv::Mat& depth) {

	// ========== color convert RTC -> opencv ==============
	int len = rtc_depth.width * rtc_depth.height * rtc_depth.bpp;
	cv::Size imageSize = cv::Size(rtc_depth.width, rtc_depth.height);
	depth = cv::Mat(imageSize, CV_16UC1);

	memcpy(depth.data, (void*) &(rtc_depth.pixels[0]), len);
}
void cvt_RTCir_to_CVir(RTC::CameraImage& rtc_ir, cv::Mat& ir) {

	// ========== color convert RTC -> opencv ==============
	int len = rtc_ir.width * rtc_ir.height * rtc_ir.bpp;
	cv::Size imageSize = cv::Size(rtc_ir.width, rtc_ir.height);
	std::string tmp(rtc_ir.format);
	std::cout << tmp << std::endl;

	if(tmp == "Y8")
		ir = cv::Mat(imageSize, CV_8UC1);
	else if(tmp == "Y16")
		ir = cv::Mat(imageSize, CV_16UC1);

	memcpy(ir.data, (void*) &(rtc_ir.pixels[0]), len);

}

