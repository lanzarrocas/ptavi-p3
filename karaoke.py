#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal:
    def __init__(self, f_name):
        if os.path.exists(f_name):
            parser = make_parser()
            cHandler = SmallSMILHandler()
            parser.setContentHandler(cHandler)
            parser.parse(open(f_name))
            self.tags = cHandler.get_tags()
        else:
            sys.exit("File not found")

    def __str__(self):
        line = ""
        for tag in self.tags:
            line += tag[0]
            for att in tag[1]:
                if tag[1][att] != "":
                    line += "\t" + att + "=\"" + tag[1][att] + "\""
            line += "\n"
        return line


if __name__ == "__main__":
    if len(sys.argv) == 2:
        f_smil = sys.argv[1]
        if ".smil" in f_smil:
            f_json = f_smil.replace("smil", "json")
        else:
            sys.exit("not smil file")
    else:
        sys.exit("Usage Error: python3 karaoke.py file.smil")

    karaoke = KaraokeLocal(f_smil)
    print(karaoke)
    with open(f_json, "w") as jsonfile:
        json.dump(karaoke.tags, jsonfile, indent=2)
