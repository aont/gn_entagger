#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
import os

gnsdk_path = os.path.dirname(__file__)
prev_dir = os.getcwd()
os.chdir(gnsdk_path)
_dll = ctypes.WinDLL('gnsdk_manager.dll')
os.chdir(prev_dir)

_dll.gnsdk_manager_get_version.argtypes = None
_dll.gnsdk_manager_get_version.restype = ctypes.c_char_p
get_version = _dll.gnsdk_manager_get_version

_dll.gnsdk_manager_initialize.restype = ctypes.c_uint
_dll.gnsdk_manager_initialize.argtypes = [ctypes.POINTER(ctypes.c_uint64), ctypes.c_char_p, ctypes.c_int64]
initialize = _dll.gnsdk_manager_initialize

_dll.gnsdk_manager_user_register.restype = ctypes.c_uint
_dll.gnsdk_manager_user_register.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]
user_register = _dll.gnsdk_manager_user_register

_dll.gnsdk_manager_user_create.restype = ctypes.c_uint
_dll.gnsdk_manager_user_create.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint64)]
user_create = _dll.gnsdk_manager_user_create

_dll.gnsdk_manager_user_release.restype = ctypes.c_uint
_dll.gnsdk_manager_user_release.argtypes = [ctypes.c_uint64]
user_release = _dll.gnsdk_manager_user_release

_dll.gnsdk_manager_shutdown.restype = ctypes.c_uint
_dll.gnsdk_manager_shutdown.argtypes = None
shutdown = _dll.gnsdk_manager_shutdown

_dll.gnsdk_manager_user_option_set.restype = ctypes.c_uint
_dll.gnsdk_manager_user_option_set.argtypes = [ctypes.c_uint64, ctypes.c_char_p, ctypes.c_char_p]
user_option_set = _dll.gnsdk_manager_user_option_set

FALSE='0'
TRUE='1'
