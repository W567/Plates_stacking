#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "RTC_ImageProcess" for configuration ""
set_property(TARGET RTC_ImageProcess APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(RTC_ImageProcess PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NOCONFIG "pthread;omniORB4;omnithread;omniDynamic4;RTC;coil;opencv_flann;opencv_videostab;opencv_core;opencv_objdetect;opencv_photo;opencv_highgui;opencv_imgproc;opencv_dnn;opencv_shape;opencv_stitching;opencv_calib3d;opencv_imgcodecs;opencv_superres;opencv_viz;opencv_features2d;opencv_ml;opencv_videoio;opencv_video"
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/components/lib/RTC_ImageProcess.so"
  IMPORTED_SONAME_NOCONFIG "RTC_ImageProcess.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS RTC_ImageProcess )
list(APPEND _IMPORT_CHECK_FILES_FOR_RTC_ImageProcess "${_IMPORT_PREFIX}/components/lib/RTC_ImageProcess.so" )

# Import target "RTC_ImageProcessComp" for configuration ""
set_property(TARGET RTC_ImageProcessComp APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(RTC_ImageProcessComp PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/components/bin/RTC_ImageProcessComp"
  )

list(APPEND _IMPORT_CHECK_TARGETS RTC_ImageProcessComp )
list(APPEND _IMPORT_CHECK_FILES_FOR_RTC_ImageProcessComp "${_IMPORT_PREFIX}/components/bin/RTC_ImageProcessComp" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
