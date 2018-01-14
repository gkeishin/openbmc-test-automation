*** Settings ***

Documentation  Test Open BMC GUI Power Operations under GUI Header.

Resource  ../../lib/resource.robot

Suite Setup  Login OpenBMC GUI  ${OPENBMC_USERNAME}  ${OPENBMC_PASSWORD}
Suite Teardown  Close Browser

*** Test Cases ***

Power On The Host
    [Documentation]  Power on the host.
    [Tags]  Power_On_the_Host

    GUI Power On

Click Immediate Power Off The Host And Press No
    [Documentation]  Click Immediate power off the host button and press no
    ...  button.
    [Tags]  Click_Immediate_Power_Off_The_Host_And_Press_No

    Controller Server Power Click Button  power__hard-shutdown
    Controller Power Operations Confirmation Click Button  ${power_operations}
    ...  ${power_off}  ${confirm_msg}  ${no}
    Page Should Contain  Running

Click Immediate Power Off The Host And Press Yes
    [Documentation]  Click Immediate power off the host button and press
    ...  yes button.
    [Tags]  Click_Immediate_Power_Off_The_Host_And_Press_Yes

    Controller Server Power Click Button  power__hard-shutdown
    Controller Power Operations Confirmation Click Button  ${power_operations}
    ...  ${power_off}  ${confirm_msg}  ${yes}
    Page Should Contain  Off

Click Cold Boot The Host And Press No
    [Documentation]  Click cold boot the host button and press no button.
    [Tags]  Click_Cold_Boot_The_Host_And_Press_No

    GUI Power On
    Controller Server Power Click Button  power__cold-boot
    Controller Power Operations Confirmation Click Button  ${power_operations}
    ...  ${cold_boot}  ${confirm_msg}  ${no}
    Page Should Contain  Running

Click Cold Boot The Host And Press Yes
    [Documentation]  Click Cold boot the host button and press yes button.
    [Tags]  Click_Cold_Boot_the_Host_And_Press_Yes

    Controller Server Power Click Button  power__cold-boot
    Controller Power Operations Confirmation Click Button  ${power_operations}
    ...  ${cold_boot}  ${confirm_msg}  ${yes}
    Page Should Contain  Standby
    Page Should Contain  Running

Click Warm Boot The Host And Press No
    [Documentation]  Click warm boot the host button and press no button.
    [Tags]  Click_Warm_Boot_The_Host_And_Press_No

    Controller Server Power Click Button  power__warm-boot
    Controller Power Operations Confirmation Click Button  ${power_operations}
    ...  ${warm_boot}  ${confirm_msg}  ${no}
    Page Should Contain  Running

Click Warm Boot The Host And Press Yes
    [Documentation]  Click warm boot the host button and press yes button.
    [Tags]  Click_Warm_Boot_The_Host_And_Press_Yes

    Controller Server Power Click Button  power__warm-boot
    Controller Power Operations Confirmation Click Button  ${power_operations}
    ...  ${warm_boot}  ${confirm_msg}  ${yes}
    Page Should Contain  Running

Click Orderly Shutdown The Host And Press No
    [Documentation]  Press orderly shutdown the host button and press no
    ...  button.
    [Tags]  Click_Orderly_Shutdown_The_Host_And_Press_No

    Controller Server Power Click Button  power__soft-shutdown
    Controller Power Operations Confirmation Click Button  ${power_operations}
    ...  ${shut_down}  ${confirm_msg}  ${no}
    Page Should Contain  Running

Click Orderly Shutdown The Host And Press Yes
    [Documentation]  Press orderly shutdown the host button and press yes
    ...  button.
    [Tags]  Click_Orderly_Shutdown_The_Host_And_Press_Yes

    Controller Server Power Click Button  power__soft-shutdown
    Controller Power Operations Confirmation Click Button  ${power_operations}
    ...  ${shut_down}  ${confirm_msg}  ${yes}
    Page Should Contain  Off

OpenBMC GUI Logoff
    [Documentation]  Log out from openBMC GUI.
    [Tags]  OpenBMC_GUI_Logoff

    Log  ${xpath_openbmc_url}
    Log To Console  ${xpath_openbmc_url}
    Click Element  header




