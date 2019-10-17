#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import requests
import os
import shutil
# import lxml
# import lxml.etree
import json
import argparse

import mutagen
import mutagen.id3
import mutagen.mp3

def check_none(obj):
    if obj is None:
        raise Exception("None unexpectedly!")
    else:
        return obj

def valid_fn(fn):
    return fn.replace("\\", "¥").replace("/", "／").replace(":", "：").replace("*", "＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜")

def entag(json_path, idx_album_p1, stderr = os.devnull):
    # cwd = os.getcwd() 

    idx_album = idx_album_p1 - 1
    target_dir = os.path.dirname(json_path)

    # idx_album = 0
    with open(json_path, "r", encoding='utf-8') as f_json:
        album_ary = json.load(f_json)
        
    #(sys.stdin)
    album_i = check_none(album_ary[idx_album].get("ALBUM"))
    
    album_title = check_none(album_i.get("TITLE_OFFICIAL").get("DISPLAY"))
    stderr.write("[info] album_title=%s\n" % album_title)
    album_artist = check_none(album_i.get("ARTIST").get("NAME_OFFICIAL").get("DISPLAY"))
    stderr.write("[info] album_artist=%s\n" % album_artist)
    # print(album_artist)
    dir_mp3_prev = os.path.join(target_dir, "mp3")
    dir_mp3 = os.path.join(target_dir, valid_fn("%s - %s" % (album_title, album_artist)))

    # os.mkdir(target_dir)
    # shutil.move(dir_mp3_prev, dir_mp3)
    os.mkdir(dir_mp3)
    # shutil.copy(dir_mp3_prev, dir_mp3)
    # os.chdir(dir_mp3)
    # os.mkdir(dir_mp3)
    # os.chdir(dir_mp3)

    track_count = check_none(int(album_i.get("TRACK_COUNT")))
    stderr.write("[info] track_count=%s\n" % track_count)
    track_ary = check_none(album_i.get("TRACK"))
    if len(track_ary) != track_count:
        raise Exception("number of tracks is inconsistent!")
    
    for idx_track in range(track_count):
        track = track_ary[idx_track]
        # ord_track = int(check_none(track.get("ORD")))
        # if (idx_track+1)!=ord_track:
        #     raise Exception("ORD is inconsistent")
        track_num = int(check_none(track.get("TRACK_NUM")))
        stderr.write("[info] track num=%s\n" % track_num)

        if (idx_track+1)!=track_num:
            raise Exception("TRACK_NUM is inconsistent")
        track_title = check_none(track.get("TITLE_OFFICIAL").get("DISPLAY"))
        stderr.write("[info] track title=%s\n" % track_title)
        track_artist_json = track.get("ARTIST")
        if track_artist_json:
            track_artist = check_none(track_artist_json.get("NAME_OFFICIAL").get("DISPLAY"))
            stderr.write("[info] track artist=%s\n" % track_artist)

        stderr.write("[info] copying...")
        prev_fn = os.path.join(dir_mp3_prev, "track%02d.mp3" % track_num)
        mp3_fn = os.path.join(dir_mp3, "%02d - %s.mp3" % (track_num, valid_fn(track_title) ) )
        shutil.copyfile(prev_fn, mp3_fn)
        stderr.write("done\n")

        stderr.write("[info] entagging...")
        mp3 = mutagen.mp3.MP3(mp3_fn, ID3=mutagen.id3.ID3)
        mp3.add_tags(ID3=mutagen.id3.ID3)
        mp3["TIT2"] = mutagen.id3.TIT2(encoding=3, text=track_title)
        #if track_artist is not None:
        if track_artist_json:
            mp3["TPE1"] = mutagen.id3.TPE1(encoding=3, text=track_artist)
        else:
            mp3["TPE1"] = mutagen.id3.TPE1(encoding=3, text=album_artist)
        #if album_title is not None:
        mp3["TALB"] = mutagen.id3.TALB(encoding=3, text=album_title)
        #if album_artist is not None:
        mp3["TPE2"] = mutagen.id3.TPE2(encoding=3, text=album_artist)
        mp3["TRCK"] = mutagen.id3.TRCK(encoding=3, text="%s/%s" %(track_num, track_count))
        mp3["TPOS"] = mutagen.id3.TPOS(encoding=3, text="%s/%s" %(album_i.get("DISC_IN_SET"), album_i.get("TOTAL_IN_SET")))

        mp3.save()
        stderr.write("done\n")

    # os.chdir(cwd)

if __name__ == u'__main__':
    # num_data
    parser = argparse.ArgumentParser(add_help=True)
    group = parser.add_argument_group("global optional arguments")
    # group.add_argument('--mp3', action='store', default='mp3', help="specify mp3 directory path")
    group.add_argument('json', action='store', default='data.json', help="specify json file path")
    group.add_argument('-i', action='store', dest='index', default=1, help="specify index number", type=int)
    args = parser.parse_args()
    # mp3_dir = args.mp3
    json_path = args.json
    index_num = args.index
    sys.stderr.write("[info] entag json=%s index=%s\n" % (json_path, index_num))
    # target_dir = "F:/20191016_CDDA/French Chamber Music - Ashkenazy Perlman Harrell"
    entag(json_path, index_num, sys.stderr)