#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import requests
import os
import lxml
import lxml.etree

class ParseState:
    INSIDE_CUE = 0
    INSIDE_FILE = 1
    INSIDE_TRACK = 2

def parse_cue(f, e):
    lba_ary = []
    parse_state = ParseState.INSIDE_CUE
    while True:

        line = f.readline()
        if line == '':
            break
            # todo
        if re.match('^\s*\\n$', line):
            continue

        if parse_state == ParseState.INSIDE_CUE:
            match = re.match('^\\s*FILE\\s+"(.+?)"\\s+(.+)\\s*\\n$', line)
            if match:
                image_fn_quote = match.group(1)
                image_type = match.group(2)
                e.write("[Info] FILE %s %s\n" % (image_fn_quote, image_type))
                parse_state = ParseState.INSIDE_FILE
                continue
            raise Exception("Exception")
        
        elif parse_state == ParseState.INSIDE_FILE:
            match = re.match('^\\s*TRACK\\s+(\\d+)\\s+(.+)\\s*\\n$', line)
            if match:
                track_num = match.group(1)
                track_type = match.group(2)
                e.write("[Info] TRACK %s %s\n" % (track_num, track_type))
                parse_state = ParseState.INSIDE_TRACK
                continue
            raise Exception("Exception")

        elif parse_state == ParseState.INSIDE_TRACK:
            match = re.match('^\\s*INDEX\\s+(\\d+)\\s+(\\d\\d):(\\d\\d):(\\d\\d)\\s*\\n$', line)
            if match:
                index_num = match.group(1)
                min_num = int(match.group(2))
                sec_num = int(match.group(3))
                frm_num = int(match.group(4))
                lba = (min_num*60+sec_num)*75+frm_num
                e.write("[Info] INDEX %s %s:%s:%s\n" % (index_num, min_num, sec_num, frm_num ))
                if index_num == '01':
                    lba_ary.append(lba)
                # parse_state = ParseState.INSIDE_TRACK
                continue
            # todo
            match = re.match('^\\s*TRACK\\s+(\\d+)\\s+(.+)\\s*\\n$', line)
            if match:
                track_num = match.group(1)
                track_type = match.group(2)
                e.write("[Info] TRACK %s %s\n" % (track_num, track_type))
                parse_state = ParseState.INSIDE_TRACK
                continue
            raise Exception("Exception")

        raise Exception("Exception")

        e.write("[Info] line = %s" % line)
    return {"frame": lba_ary, "image": image_fn_quote}

def len_cdda(path):
    img_size = os.path.getsize(path)
    return int((img_size * 75)/(44100*2*2))

def acquire_disc_toc(cue, e):
    cue_f = open(cue, u'r')
    cue_data  = parse_cue(cue_f, e)
    cue_f.close()
    frame_ary = cue_data.get("frame")
    img = os.path.join(os.path.dirname(cue), cue_data.get("image"))
    lba_end = len_cdda(img)
    # for i in range(len(frame_ary)):
    #     frame_ary[i] += 150
    frame_ary.append(lba_end)
    frame_ary[0] = 150
    return frame_ary
    

# if __name__ == u'__main__':
#     data_dir = 'F:/20191016_CDDA/French Chamber Music - Ashkenazy Perlman Harrell'
#     cue = os.path.join(data_dir, "image.cue")
#     img = os.path.join(data_dir, "image.img")

#     frame_ary = acquire_disc_toc(cue, img)
#     sys.stdout.write("%s\n" % " ".join(map(lambda x: str(x), frame_ary)))
