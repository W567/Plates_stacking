# Install script for directory: /home/wu/Workspace/wu/rtc/RTC_PointCloudProcess/include/RTC_PointCloudProcess

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "library")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/components/include/rtc_pointcloudprocess-2/rtc_pointcloudprocess" TYPE FILE FILES
    "/home/wu/Workspace/wu/rtc/RTC_PointCloudProcess/include/RTC_PointCloudProcess/RTC_PointCloudProcess.h"
    "/home/wu/Workspace/wu/rtc/RTC_PointCloudProcess/include/RTC_PointCloudProcess/PARENT_SCOPE"
    "/home/wu/Workspace/wu/rtc/RTC_PointCloudProcess/include/RTC_PointCloudProcess/pcProcessPortSVC_impl.h"
    )
endif()

