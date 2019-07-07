#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import config


import gnsdk_musicid
import gnsdk_manager
import gnsdk_manager_gdo
import ctypes

toc = '150 38965 71212 109050 145390 166165 194777 230065 256465 269015'

ver = gnsdk_manager.get_version()
sys.stderr.write("[Info] gnsdk_manager_get_version=%s\n" % ver.decode('utf-8'))

ver = gnsdk_musicid.get_version()
sys.stderr.write("[Info] gnsdk_musicid_get_version=%s\n" % ver.decode('utf-8'))

sdkmgr_handle = ctypes.c_uint64()
sdkmgr_handle.value = 123
err = gnsdk_manager.initialize(
    sdkmgr_handle, config.license.encode('utf-8'), len(config.license))
sys.stderr.write("[Info] gnsdk_manager_initialize=0x%X sdkmgr_handle=0x%X\n" % (err, sdkmgr_handle.value))
if err != 0:
    raise Exception("Exception")

err = gnsdk_musicid.initialize(sdkmgr_handle.value)
sys.stderr.write("[Info] gnsdk_musicid_initialize(sdkmgr_handle)=0x%X\n" % err)
if err != 0:
    raise Exception("Exception")

if True:
    err = gnsdk_manager.user_option_set(0, "gnsdk_useroption_proxy_host".encode('utf-8'), config.proxy_host.encode('utf-8'))
    sys.stderr.write("[Info] gnsdk_manager_user_option_set(proxy host)=0x%X\n" % (err))
    if err != 0:
        raise Exception("Exception")

    err = gnsdk_manager.user_option_set(0, "gnsdk_useroption_proxy_username".encode('utf-8'), config.proxy_user.encode('utf-8'))
    sys.stderr.write("[Info] gnsdk_manager_user_option_set(proxy user)=0x%X\n" % (err))
    if err != 0:
        raise Exception("Exception")

    err = gnsdk_manager.user_option_set(0, "gnsdk_useroption_proxy_password".encode('utf-8'), config.proxy_pass.encode('utf-8'))
    sys.stderr.write("[Info] gnsdk_manager_user_option_set(proxy password)=0x%X\n" % (err))
    if err != 0:
        raise Exception("Exception")

serialized_user = ctypes.c_char_p()
err = gnsdk_manager.user_register('gnsdk_userregmode_online'.encode('utf-8'), config.client_id.encode('utf-8'), config.client_id_tag.encode('utf-8'), '1'.encode('utf-8'), serialized_user)
sys.stderr.write("[Info] gnsdk_manager_user_register()=0x%X serialized_user=%s\n" % (err, serialized_user.value.decode('utf-8')))
if err != 0:
    raise Exception("Exception")

user_handle = ctypes.c_uint64()
err = gnsdk_manager.user_create(
    serialized_user.value, config.client_id.encode('utf-8'), user_handle)
sys.stderr.write("[Info] gnsdk_manager_user_create(serialized_user, client_id)=0x%X user_handle=0x%X\n" % (err, user_handle.value))
if err != 0:
    raise Exception("Exception")

query_handle = ctypes.c_uint64()
err = gnsdk_musicid.query_create(user_handle.value, None, None, query_handle)
sys.stderr.write("[Info] gnsdk_musicid_query_create(user_handle)=0x%X query_handle=0x%X\n" % (err, query_handle.value))
if err != 0:
    raise Exception("Exception")

err = gnsdk_musicid.query_set_toc_string(query_handle.value, toc.encode('utf-8'))
sys.stderr.write("[Info] gnsdk_musicid_query_set_toc_string(query_handle, toc)=0x%X\n" % (err))
if err != 0:
    raise Exception("Exception")

response_gdo = ctypes.c_uint64()
err = gnsdk_musicid.query_find_albums(query_handle.value, response_gdo)
sys.stderr.write("[Info] gnsdk_musicid_query_find_albums(query_handle)=0x%X response_gdo=0x%X\n" % (err, response_gdo.value))
if err != 0:
    raise Exception("Exception")

xml_str = ctypes.c_char_p()
err = gnsdk_manager_gdo.render2(response_gdo.value, 1, gnsdk_manager_gdo.RENDER_XML | gnsdk_manager_gdo.RENDER_FULL, xml_str)
sys.stderr.write("[Info] gnsdk_manager_gdo_render2(response_gdo)=0x%X\n" % (err))
sys.stdout.write(xml_str.value.decode('utf-8'))
if err != 0:
    raise Exception("Exception")


count = ctypes.c_uint32()
err = gnsdk_manager_gdo.child_count(response_gdo.value, gnsdk_manager_gdo.CHILD_ALBUM.encode('utf-8'), count)
sys.stderr.write("[Info] gnsdk_manager_gdo_child_count(response_gdo, gnsdk_manager_gdo.CHILD_ALBUM)=0x%X count=%d\n" % (err, count.value))
if err != 0:
    raise Exception("Exception")

if count.value == 0:
    sys.stderr.write("No albums found for the input.\n")


needs_decision = ctypes.c_char_p()
err = gnsdk_manager_gdo.value_get(response_gdo.value, gnsdk_manager_gdo.VALUE_RESPONSE_NEEDS_DECISION.encode('utf-8'), 1, needs_decision)
sys.stderr.write("[Info] gnsdk_manager_gdo_value_get(response_gdo, gnsdk_manager_gdo.VALUE_RESPONSE_NEEDS_DECISION)=0x%X needs_decision=%s\n" % (err, needs_decision.value.decode('utf-8')))
if err != 0:
    raise Exception("Exception")


sys.stdout.write("<OUTPUT>\n")
for choice in range(count.value):

    # if GNSDK_VALUE_TRUE == needs_decision.value:
    #         choice_ordinal = 1 # _do_match_selection(response_gdo.value)
    # else:
    #         choice_ordinal = 1

    album_gdo = ctypes.c_uint64()
    err = gnsdk_manager_gdo.child_get(response_gdo.value, gnsdk_manager_gdo.CHILD_ALBUM.encode('utf-8'), choice+1, album_gdo)
    sys.stderr.write("[Info] gnsdk_manager_gdo_child_get(response_gdo, gnsdk_manager_gdo.CHILD_ALBUM, %s)=0x%X album_gdo=0x%X\n" % (choice+1, err, album_gdo.value))
    if err != 0:
        raise Exception("Exception")

    is_full = ctypes.c_char_p()
    err = gnsdk_manager_gdo.value_get(album_gdo.value, gnsdk_manager_gdo.VALUE_FULL_RESULT.encode('utf-8'), choice+1, is_full)
    sys.stderr.write("[Info] gnsdk_manager_gdo_value_get(album_gdo, gnsdk_manager_gdo.VALUE_FULL_RESULT, %s)=0x%X is_full=%s\n" % (choice+1, err, is_full.value))
    # if err != 0:
    #         raise Exception("Exception")
    # if GNSDK_VALUE_FALSE == is_full.value:
    if False:
        err = gnsdk_musicid.query_set_gdo(query_handle.value, album_gdo.value)
        sys.stderr.write("[Info] gnsdk_musicid_query_set_gdo(query_handle, album_gdo)=0x%X\n" % (err))
        if err != 0:
            raise Exception("Exception")

        err = gnsdk_manager_gdo.release(album_gdo)
        sys.stderr.write("[Info] gnsdk_manager_gdo_release(album_gdo)=0x%X\n" % (err))
        if err != 0:
            raise Exception("Exception")
        # album_gdo.value = 0

        followup_response_gdo = ctypes.c_uint64()
        err = gnsdk_musicid.query_find_albums(query_handle.value, followup_response_gdo)
        sys.stderr.write("[Info] gnsdk_musicid_query_find_albums(query_handle)=0x%X 0x%X\n" % (err, response_gdo.value))
        if err != 0:
            raise Exception("Exception")

        xml_str = ctypes.c_char_p()
        err = gnsdk_manager_gdo.render2(followup_response_gdo.value, 1, gnsdk_manager_gdo.RENDER_XML | gnsdk_manager_gdo.RENDER_FULL, xml_str)
        sys.stderr.write("[Info] gnsdk_manager_gdo_render2(followup_response_gdo)=0x%X\n" % (err))
        sys.stdout.write(xml_str.value.decode('utf-8'))
        if err != 0:
            raise Exception("Exception")

        err = gnsdk_manager_gdo.child_get(followup_response_gdo.value, gnsdk_manager_gdo.CHILD_ALBUM.encode('utf-8'), 1, album_gdo)
        sys.stderr.write("[Info] gnsdk_manager_gdo_child_get(followup_response_gdo)=0x%X album_gdo=0x%X\n" % (err, album_gdo.value))
        if err != 0:
            raise Exception("Exception")

        err = gnsdk_manager_gdo.release(followup_response_gdo.value)
        sys.stderr.write("[Info] gnsdk_manager_gdo_release(followup_response_gdo)=0x%X\n" % (err))
        if err != 0:
            raise Exception("Exception")

    xml_str = ctypes.c_char_p()
    err = gnsdk_manager_gdo.render2(album_gdo.value, 1, gnsdk_manager_gdo.RENDER_XML | gnsdk_manager_gdo.RENDER_FULL, xml_str)
    sys.stderr.write("[Info] gnsdk_manager_gdo_render2(album_gdo)=0x%X\n" % (err))
    sys.stdout.write(xml_str.value.decode('utf-8'))
    if err != 0:
        raise Exception("Exception")

    err = gnsdk_manager_gdo.release(album_gdo.value)
    sys.stderr.write("[Info] gnsdk_manager_gdo_release(album_gdo)=0x%X\n" % (err))
    if err != 0:
        raise Exception("Exception")

sys.stdout.write("</OUTPUT>\n")

err = gnsdk_musicid.query_release(query_handle.value)
sys.stderr.write("[Info] gnsdk_musicid_query_release(query_handle)= 0x%X\n" % (err))
if err != 0:
    raise Exception("Exception")

err = gnsdk_manager_gdo.release(response_gdo.value)
sys.stderr.write("[Info] gnsdk_manager_gdo_release(response_gdo)=0x%X\n" % (err))
if err != 0:
    raise Exception("Exception")

err = gnsdk_musicid.shutdown()
sys.stderr.write("[Info] gnsdk_musicid_shutdown= 0x%X\n" % (err))
if err != 0:
    raise Exception("Exception")

err = gnsdk_manager.user_release(user_handle.value)
sys.stderr.write("[Info] gnsdk_manager_user_release= 0x%X\n" % err)
if err != 0:
    raise Exception("Exception")

err = gnsdk_manager.shutdown()
sys.stderr.write("[Info] gnsdk_manager_shutdown= 0x%X\n" % (err))
if err != 0:
    raise Exception("Exception")
