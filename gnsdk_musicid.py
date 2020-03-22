#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
import os

gnsdk_path = os.path.dirname(__file__)
prev_dir = os.getcwd()
os.chdir(gnsdk_path)
_dll = ctypes.WinDLL('gnsdk_musicid.dll')
os.chdir(prev_dir)

_dll.gnsdk_musicid_initialize.restype = ctypes.c_uint
_dll.gnsdk_musicid_initialize.argtypes = [ctypes.c_uint64]
initialize = _dll.gnsdk_musicid_initialize

_dll.gnsdk_musicid_shutdown.restype = ctypes.c_uint
_dll.gnsdk_musicid_shutdown.argtypes = None
shutdown = _dll.gnsdk_musicid_shutdown

_dll.gnsdk_musicid_get_version.restype = ctypes.c_char_p
_dll.gnsdk_musicid_get_version.argtypes = None
get_version = _dll.gnsdk_musicid_get_version


_dll.gnsdk_musicid_query_create.restype = ctypes.c_uint
_dll.gnsdk_musicid_query_create.argtypes = [ctypes.c_uint64, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64)]
query_create = _dll.gnsdk_musicid_query_create
# todo: callback ctypes.WINFUNCTYPE()

_dll.gnsdk_musicid_query_release.restype = ctypes.c_uint
_dll.gnsdk_musicid_query_release.argtypes = [ctypes.c_uint64]
query_release = _dll.gnsdk_musicid_query_release

_dll.gnsdk_musicid_query_set_toc_string.restype = ctypes.c_uint
_dll.gnsdk_musicid_query_set_toc_string.argtypes = [ctypes.c_uint64, ctypes.c_char_p]
query_set_toc_string = _dll.gnsdk_musicid_query_set_toc_string

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_add_toc_offset(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle,
# 	gnsdk_uint32_t					toc_offset
# 	);

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_set_text(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle,
# 	gnsdk_cstr_t					search_field,
# 	gnsdk_cstr_t					search_text
# 	);

FIELD_ALBUM_ARTIST = "gnsdk_musicid_field_album_artist"
FIELD_TRACK_ARTIST = "gnsdk_musicid_field_track_artist"
FIELD_ALBUM = "gnsdk_musicid_field_album"
FIELD_TITLE = "gnsdk_musicid_field_title"
FIELD_COMPOSER = "gnsdk_musicid_field_composer"
FIELD_LYRIC_FRAGMENT = "gnsdk_musicid_field_fragment"
FIELD_ARTIST = "gnsdk_musicid_field_artist" # deprecated

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_set_fp_data(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle,
# 	gnsdk_cstr_t					fp_data,
# 	gnsdk_cstr_t					fp_data_type
# 	);

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_get_fp_data(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle,
# 	gnsdk_cstr_t					*p_fp_data
# 	);

FP_DATA_TYPE_STREAM3 = "gnsdk_musicid_fp_3stream"
FP_DATA_TYPE_STREAM6 = "gnsdk_musicid_fp_6stream"
FP_DATA_TYPE_GNFPX = FP_DATA_TYPE_STREAM3
FP_DATA_TYPE_STREAMFP = "gnsdk_musicid_fp_streamfp"
FP_DATA_TYPE_FILE = "gnsdk_musicid_fp_file"
FP_DATA_TYPE_CMX = FP_DATA_TYPE_FILE

query_set_gdo = _dll.gnsdk_musicid_query_set_gdo
query_set_gdo.restype = ctypes.c_uint
query_set_gdo.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
# _dll.gnsdk_musicid_query_set_gdo(query_handle.value, album_gdo.value)
# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_set_gdo(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle,
# 	gnsdk_gdo_handle_t				query_gdo
# 	);

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_set_locale(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle,
# 	gnsdk_locale_handle_t			locale_handle
# 	);

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_fingerprint_begin(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle,
# 	gnsdk_cstr_t					fp_data_type,
# 	gnsdk_uint32_t					audio_sample_rate,
# 	gnsdk_uint32_t					audio_sample_size,
# 	gnsdk_uint32_t					audio_channels
# 	);

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_fingerprint_write(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle,
# 	const gnsdk_void_t*				audio_data,
# 	gnsdk_size_t					audio_data_size,
# 	gnsdk_bool_t*					pb_complete
# 	);

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_fingerprint_end(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle
# 	);

#  GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_fingerprint_info_get(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle,
# 	gnsdk_cstr_t					info_key,
# 	gnsdk_cstr_t*					p_info_value
# 	);

AUDIO_INFO_SUITABLE_FOR_QUERY = "gnsdk_musicid_query_fp_info_suitable_for_query"

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_option_set(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle,
# 	gnsdk_cstr_t					option_key,
# 	gnsdk_cstr_t					option_value
# 	);

# GNSDK_EXPORTED gnsdk_error_t GNSDK_API
# gnsdk_musicid_query_option_get(
# 	gnsdk_musicid_query_handle_t	musicid_query_handle,
# 	gnsdk_cstr_t					option_key,
# 	gnsdk_cstr_t*					p_option_value
# 	);

# OPTION_LOOKUP_MODE = GNSDK_QUERY_OPTION_LOOKUP_MODE
OPTION_ENABLE_CLASSICAL_DATA = "gnsdk_musicid_option_enable_classical"
OPTION_INLINE_IMAGE_SIZE = "gnsdk_musicid_option_inline_image_size"
OPTION_ENABLE_GLOBALIDS = "gnsdk_musicid_option_enable_globalids"
OPTION_ENABLE_SONIC_DATA = "gnsdk_musicid_option_enable_sonic"
OPTION_ENABLE_DSP_DATA = "gnsdk_musicid_option_enable_dsp"
OPTION_ENABLE_PLAYLIST = "gnsdk_musicid_option_enable_playlist"
OPTION_ENABLE_EXTERNAL_IDS = "gnsdk_musicid_option_enable_xids"
OPTION_ENABLE_CONTENT_DATA = "gnsdk_musicid_option_enable_content"
OPTION_ENABLE_SORTABLE = "gnsdk_musicid_option_enable_sortable"
OPTION_ENABLE_LINK_DATA = "gnsdk_musicid_option_enable_link"
OPTION_ADDITIONAL_CREDITS = "gnsdk_musicid_option_additional_credits"
OPTION_PREFerrED_LANG = "gnsdk_musicid_preferred_lang"
OPTION_RESULT_SINGLE = "gnsdk_musicid_single_result"
OPTION_RESULT_PREFER_XID = "gnsdk_musicid_result_prefer_xid"
OPTION_RESULT_PREFER_COVERART = "gnsdk_musicid_result_prefer_coverart"
OPTION_RESULT_RANGE_START = "gnsdk_musicid_result_range_start"
#801


_dll.gnsdk_musicid_query_find_matches.restype = ctypes.c_uint
_dll.gnsdk_musicid_query_find_matches.argtypes = [ctypes.c_uint64, ctypes.POINTER(ctypes.c_uint64)]
query_find_matches = _dll.gnsdk_musicid_query_find_matches

_dll.gnsdk_musicid_query_find_albums.restype = ctypes.c_uint
_dll.gnsdk_musicid_query_find_albums.argtypes = [ctypes.c_uint64, ctypes.POINTER(ctypes.c_uint64)]
query_find_albums = _dll.gnsdk_musicid_query_find_albums
