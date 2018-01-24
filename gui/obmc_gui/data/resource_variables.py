#!/usr/bin/python

r"""
Contains xpaths and related string constants applicable to all openBMC GUI
menus.
"""


class resource_variables():

    xpath_textbox_hostname = "//*[@id='login__form']/input[1]"
    xpath_textbox_username = "//*[@id='username']"
    xpath_textbox_password = "//*[@id='password']"
    xpath_button_login = "//*[@id='login__submit']"
    xpath_button_logout = "//*[@id='header']/a"
    xpath_openbmc_url = "http://localhost:8080/#/login"
    xpath_openbmc_ip = "//*[@id='login__form']/input[1]"
    xpath_display_server_power_status = \
        "//*[@id='header__wrapper']/div/div[3]/a[3]/span"
    xpath_select_button_power_on = "//*[@id='power__power-on']"

    xpath_select_button_warm_reboot = \
        "//*[@id='power__warm-boot']"
    xpath_warm_reboot_warning_message = \
        "//*[@id='power-operations']" \
        "/div[3]/div[3]/confirm/div/div[1]/p[1]/strong"
    xpath_select_button_warm_reboot_no = \
        "//*[@id='power-operations']/div[3]" \
        "/div[3]/confirm/div/div[2]/button[2]"
    text_warm_reboot_warning_message = "warm reboot?"
    xpath_select_button_warm_reboot_yes = \
        "//*[@id='power-operations']" \
        "/div[3]/div[3]/confirm/div/div[2]/button[1]"

    xpath_select_button_cold_reboot = \
        "//*[@id='power__cold-boot']"
    xpath_cold_reboot_warning_message = \
        "//*[@id='power-operations']/div[3]/div[4]" \
        "/confirm/div/div[1]/p[1]/strong"
    xpath_select_button_cold_reboot_no = \
        "//*[@id='power-operations']/div[3]/div[4]" \
        "/confirm/div/div[2]/button[2]"
    text_cold_reboot_warning_message = "cold reboot?"
    xpath_select_button_cold_reboot_yes = \
        "//*[@id='power-operations']" \
        "/div[3]/div[4]/confirm/div/div[2]/button[2]"

    xpath_select_button_orderly_shutdown = \
        "//*[@id='power__soft-shutdown']"
    xpath_orderly_shutdown_warning_message = \
        "//*[@id='power-operations']/div[3]/div[5]/" \
        "confirm/div/div[1]/p[1]/strong"
    xpath_select_button_orderly_shutdown_button_no = \
        "//*[@id='power-operations']/div[3]/div[5]"\
        "/confirm/div/div[2]/button[2]"
    text_orderly_shutdown_warning_message = "orderly shutdown?"
    xpath_select_button_orderly_shutdown_yes = \
        "//*[@id='power-operations']/div[3]/div[5]" \
        "/confirm/div/div[2]/button[1]"

    xpath_select_button_immediate_shutdown = \
        "//*[@id='power__hard-shutdown']"
    xpath_immediate_shutdown_warning_message = \
        "//*[@id='power-operations']/div[3]/div[6]" \
        "/confirm/div/div[1]/p[1]/strong"
    xpath_select_button_immediate_shutdown_no = \
        "//*[@id='power-operations']/div[3]/div[6]" \
        "/confirm/div/div[2]/button[2]"
    text_immediate_shutdown_warning_message = "immediate shutdown?"
    xpath_select_button_immediate_shutdown_yes = \
        "//*[@id='power-operations']/div[3]/div[6]" \
        "/confirm/div/div[2]/button[1]"

    obmc_off_state = "Off"
    obmc_standby_state = "Standby"
    obmc_running_state = "Running"

    # Power operation elements needed for power on.
    header_wrapper = "3"
    header_wrapper_elt = "3"

    # Power operation elements needed for power operations confirmation.
    power_operations = "3"
    warm_boot = "3"
    cold_boot = "4"
    shut_down = "5"
    power_off = "6"
    confirm_msg = "2"
    yes = "1"
    No = "2"
