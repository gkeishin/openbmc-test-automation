#!/usr/bin/env python

r"""
This module provides many valuable bmc ssh functions such as
bmc_execute_command.
"""

import sys
import exceptions
import re
import gen_print as gp
import gen_valid as gv
import gen_robot_ssh as grs
from robot.libraries.BuiltIn import BuiltIn


###############################################################################
def bmc_execute_command(cmd_buf,
                        print_out=0,
                        print_err=0,
                        ignore_err=0,
                        fork=0,
                        quiet=None,
                        test_mode=None):

    r"""
    Run the given command in an BMC SSH session and return the stdout, stderr
    and the return code.

    This function will obtain the global values for OPENBMC_HOST,
    OPENBMC_USERNAME, etc.

    Description of arguments:
    cmd_buf                         The command string to be run in an SSH
                                    session.
    print_out                       If this is set, this function will print
                                    the stdout/stderr generated by the shell
                                    command.
    print_err                       If show_err is set, this function will
                                    print a standardized error report if the
                                    shell command returns non-zero.
    ignore_err                      Indicates that errors encountered on the
                                    sshlib.execute_command are to be ignored.
    fork                            Indicates that sshlib.start is to be used
                                    rather than sshlib.execute_command.
    quiet                           Indicates whether this function should run
                                    the pissuing() function prints an
                                    "Issuing: <cmd string>" to stdout.  This
                                    defaults to the global quiet value.
    test_mode                       If test_mode is set, this function will
                                    not actually run the command.  This
                                    defaults to the global test_mode value.
    """

    # Get global BMC variable values.
    openbmc_host = BuiltIn().get_variable_value("${OPENBMC_HOST}", default="")
    openbmc_username = BuiltIn().get_variable_value("${OPENBMC_USERNAME}",
                                                    default="")
    openbmc_password = BuiltIn().get_variable_value("${OPENBMC_PASSWORD}",
                                                    default="")

    if not gv.valid_value(openbmc_host):
        return "", "", 1
    if not gv.valid_value(openbmc_username):
        return "", "", 1
    if not gv.valid_value(openbmc_password):
        return "", "", 1

    open_connection_args = {'host': openbmc_host, 'alias': 'bmc_connection',
                            'timeout': '25.0', 'prompt': '# '}
    login_args = {'username': openbmc_username, 'password': openbmc_password}

    return grs.execute_ssh_command(cmd_buf, open_connection_args, login_args,
                                   print_out, print_err, ignore_err, fork,
                                   quiet, test_mode)

###############################################################################


###############################################################################
def os_execute_command(cmd_buf,
                       print_out=0,
                       print_err=0,
                       ignore_err=0,
                       fork=0,
                       quiet=None,
                       test_mode=None):

    r"""
    Run the given command in an OS SSH session and return the stdout, stderr
    and the return code.

    This function will obtain the global values for OS_HOST, OS_USERNAME, etc.

    Description of arguments:
    cmd_buf                         The command string to be run in an SSH
                                    session.
    print_out                       If this is set, this function will print
                                    the stdout/stderr generated by the shell
                                    command.
    print_err                       If show_err is set, this function will
                                    print a standardized error report if the
                                    shell command returns non-zero.
    ignore_err                      Indicates that errors encountered on the
                                    sshlib.execute_command are to be ignored.
    fork                            Indicates that sshlib.start is to be used
                                    rather than sshlib.execute_command.
    quiet                           Indicates whether this function should run
                                    the pissuing() function prints an
                                    "Issuing: <cmd string>" to stdout.  This
                                    defaults to the global quiet value.
    test_mode                       If test_mode is set, this function will
                                    not actually run the command.  This
                                    defaults to the global test_mode value.
    """

    # Get global OS variable values.
    os_host = BuiltIn().get_variable_value("${OS_HOST}", default="")
    os_username = BuiltIn().get_variable_value("${OS_USERNAME}",
                                               default="")
    os_password = BuiltIn().get_variable_value("${OS_PASSWORD}",
                                               default="")

    if not gv.valid_value(os_host):
        return "", "", 1
    if not gv.valid_value(os_username):
        return "", "", 1
    if not gv.valid_value(os_password):
        return "", "", 1

    open_connection_args = {'host': os_host, 'alias': 'os_connection'}
    login_args = {'username': os_username, 'password': os_password}

    return grs.execute_ssh_command(cmd_buf, open_connection_args, login_args,
                                   print_out, print_err, ignore_err, fork,
                                   quiet, test_mode)

###############################################################################


###############################################################################
def xcat_execute_command(cmd_buf,
                         print_out=0,
                         print_err=0,
                         ignore_err=0,
                         fork=0,
                         quiet=None,
                         test_mode=None):

    r"""
    Run the given command in an XCAT SSH session and return the stdout, stderr
    and the return code.

    This function will obtain the global values for XCAT_HOST, XCAT_USERNAME,
    etc.

    Description of arguments:
    cmd_buf                         The command string to be run in an SSH
                                    session.
    print_out                       If this is set, this function will print
                                    the stdout/stderr generated by the shell
                                    command.
    print_err                       If show_err is set, this function will
                                    print a standardized error report if the
                                    shell command returns non-zero.
    ignore_err                      Indicates that errors encountered on the
                                    sshlib.execute_command are to be ignored.
    fork                            Indicates that sshlib.start is to be used
                                    rather than sshlib.execute_command.
    quiet                           Indicates whether this function should run
                                    the pissuing() function prints an
                                    "Issuing: <cmd string>" to stdout.  This
                                    defaults to the global quiet value.
    test_mode                       If test_mode is set, this function will
                                    not actually run the command.  This
                                    defaults to the global test_mode value.
    """

    # Get global XCAT variable values.
    xcat_host = BuiltIn().get_variable_value("${XCAT_HOST}", default="")
    xcat_username = BuiltIn().get_variable_value("${XCAT_USERNAME}",
                                                 default="")
    xcat_password = BuiltIn().get_variable_value("${XCAT_PASSWORD}",
                                                 default="")
    xcat_port = BuiltIn().get_variable_value("${XCAT_PORT}",
                                             default="22")

    if not gv.valid_value(xcat_host):
        return "", "", 1
    if not gv.valid_value(xcat_username):
        return "", "", 1
    if not gv.valid_value(xcat_password):
        return "", "", 1
    if not gv.valid_value(xcat_port):
        return "", "", 1

    open_connection_args = {'host': xcat_host, 'alias': 'xcat_connection',
                            'port': xcat_port}
    login_args = {'username': xcat_username, 'password': xcat_password}

    return grs.execute_ssh_command(cmd_buf, open_connection_args, login_args,
                                   print_out, print_err, ignore_err, fork,
                                   quiet, test_mode)

###############################################################################
