#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    def __init__(self):
        self.dicc = {"root-layout": ["width", "height", "background-color"],
                     "region": ["id", "top", "bottom", "left", "right"],
                     "img": ["src", "region", "begin", "dur"],
                     "audio": ["src", "begin", "dur"],
                     "textstream": ["src", "region"]}

    def startElement(self, name, attrs):
        if name == "root-layout":
            pass
        elif name == "region":
            pass
        elif name == "img":
            pass
        elif name == "audio":
            pass
        elif name == "textstream":
            pass

    def get_tags(self):
        pass

if __name__ == "__main__":
    print("programa principal")
    prueba = SmallSMILHandler()
