#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
import gnsdk_manager

_dll = gnsdk_manager._dll

_dll.gnsdk_manager_gdo_child_count.restype = ctypes.c_uint
_dll.gnsdk_manager_gdo_child_count.argtypes = [ctypes.c_uint64, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32)]
child_count = _dll.gnsdk_manager_gdo_child_count

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_manager_gdo_child_get(
# 	gnsdk_gdo_handle_t	gdo_handle,
# 	gnsdk_cstr_t		child_key,
# 	gnsdk_uint32_t		ordinal,
# 	gnsdk_gdo_handle_t* p_gdo_handle
# 	);
_dll.gnsdk_manager_gdo_child_get.restype = ctypes.c_uint
_dll.gnsdk_manager_gdo_child_get.argtypes = [ctypes.c_uint64, ctypes.c_char_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint64)]
child_get = _dll.gnsdk_manager_gdo_child_get

# gnsdk_error_t GNSDK_API
# gnsdk_manager_gdo_release(
# 	gnsdk_gdo_handle_t	gdo_handle
# );
_dll.gnsdk_manager_gdo_release.restype = ctypes.c_uint
_dll.gnsdk_manager_gdo_release.argtypes = [ctypes.c_uint64]
release = _dll.gnsdk_manager_gdo_release

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_manager_gdo_deserialize(
# 	gnsdk_cstr_t		serialized_gdo,
# 	gnsdk_gdo_handle_t*	p_gdo_handle
# 	);



# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_manager_gdo_value_get(
# 	gnsdk_gdo_handle_t	gdo_handle,
# 	gnsdk_cstr_t		value_key,
# 	gnsdk_uint32_t		ordinal,
# 	gnsdk_cstr_t*		p_value
# 	);
_dll.gnsdk_manager_gdo_value_get.restype = ctypes.c_int
_dll.gnsdk_manager_gdo_value_get.argtypes = [ctypes.c_uint64, ctypes.c_char_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_char_p)]
value_get = _dll.gnsdk_manager_gdo_value_get

_dll.gnsdk_manager_gdo_render2.restype = ctypes.c_int
_dll.gnsdk_manager_gdo_render2.argtypes = [ctypes.c_uint64, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_char_p)]
render2 = _dll.gnsdk_manager_gdo_render2

RENDER_XML=0x00000
RENDER_JSON=0x10000
RENDER_NONEWLINES=0x20000
RENDER_STANDARD=0x0001
RENDER_CREDITS=0x0002
RENDER_SORTABLE=0x0004
RENDER_SERIAL_GDOS=0x0010
RENDER_PRODUCT_IDS=0x0020
RENDER_DISCOVER_SEEDS=0x0040
RENDER_RAW_TUIS=0x0080
RENDER_GNIDS=0x0100
RENDER_GNUIDS=0x0200
RENDER_GENRE_LEVEL1=0x1000
RENDER_GENRE_LEVEL2=0x2000
RENDER_GENRE_LEVEL3=0x4000
RENDER_DESCRIPTORS=0x8000
RENDER_DEFAULT=(RENDER_STANDARD|RENDER_GENRE_LEVEL2)
RENDER_FULL=(RENDER_STANDARD|RENDER_CREDITS|RENDER_SORTABLE|RENDER_GNIDS|RENDER_DESCRIPTORS)
RENDER_SUBMIT=0x80000


TYPE_RESPONSE_MATCH = 'gnsdk_ctx_response_match'
TYPE_ALBUM = "gnsdk_ctx_album"
CHILD_ALBUM = TYPE_ALBUM + "!"
CHILD_MATCH = TYPE_RESPONSE_MATCH + '!'

VALUE_RESPONSE_NEEDS_DECISION ="gnsdk_val_decision"

VALUE_FULL_RESULT="gnsdk_val_full_result"