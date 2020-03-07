# RTC_PointCloudProcess CMake config file
#
# This file sets the following variables:
# RTC_PointCloudProcess_FOUND - Always TRUE.
# RTC_PointCloudProcess_INCLUDE_DIRS - Directories containing the RTC_PointCloudProcess include files.
# RTC_PointCloudProcess_IDL_DIRS - Directories containing the RTC_PointCloudProcess IDL files.
# RTC_PointCloudProcess_LIBRARIES - Libraries needed to use RTC_PointCloudProcess.
# RTC_PointCloudProcess_DEFINITIONS - Compiler flags for RTC_PointCloudProcess.
# RTC_PointCloudProcess_VERSION - The version of RTC_PointCloudProcess found.
# RTC_PointCloudProcess_VERSION_MAJOR - The major version of RTC_PointCloudProcess found.
# RTC_PointCloudProcess_VERSION_MINOR - The minor version of RTC_PointCloudProcess found.
# RTC_PointCloudProcess_VERSION_REVISION - The revision version of RTC_PointCloudProcess found.
# RTC_PointCloudProcess_VERSION_CANDIDATE - The candidate version of RTC_PointCloudProcess found.

message(STATUS "Found RTC_PointCloudProcess-2.0.0")
set(RTC_PointCloudProcess_FOUND TRUE)

find_package(<dependency> REQUIRED)

#set(RTC_PointCloudProcess_INCLUDE_DIRS
#    "/usr/local/include/rtc_pointcloudprocess-2"
#    ${<dependency>_INCLUDE_DIRS}
#    )
#
#set(RTC_PointCloudProcess_IDL_DIRS
#    "/usr/local/include/rtc_pointcloudprocess-2/idl")
set(RTC_PointCloudProcess_INCLUDE_DIRS
    "/usr/local/include/"
    ${<dependency>_INCLUDE_DIRS}
    )
set(RTC_PointCloudProcess_IDL_DIRS
    "/usr/local/include//idl")


if(WIN32)
    set(RTC_PointCloudProcess_LIBRARIES
        "/usr/local/components/lib/librtc_pointcloudprocess.a"
        ${<dependency>_LIBRARIES}
        )
else(WIN32)
    set(RTC_PointCloudProcess_LIBRARIES
        "/usr/local/components/lib/librtc_pointcloudprocess.so"
        ${<dependency>_LIBRARIES}
        )
endif(WIN32)

set(RTC_PointCloudProcess_DEFINITIONS ${<dependency>_DEFINITIONS})

set(RTC_PointCloudProcess_VERSION 2.0.0)
set(RTC_PointCloudProcess_VERSION_MAJOR 2)
set(RTC_PointCloudProcess_VERSION_MINOR 0)
set(RTC_PointCloudProcess_VERSION_REVISION 0)
set(RTC_PointCloudProcess_VERSION_CANDIDATE )

