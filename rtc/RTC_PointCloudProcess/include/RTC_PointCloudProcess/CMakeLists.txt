set(hdrs RTC_PointCloudProcess.h
    PARENT_SCOPE
    pcProcessPortSVC_impl.h
    )

install(FILES ${hdrs} DESTINATION ${INC_INSTALL_DIR}/${PROJECT_NAME_LOWER}
    COMPONENT library)

