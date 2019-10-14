#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    def __init__(self):
        self.list = []
        self.dicc = {"root-layout": ["width", "height", "background-color"],
                     "region": ["id", "top", "bottom", "left", "right"],
                     "img": ["src", "region", "begin", "dur"],
                     "audio": ["src", "begin", "dur"],
                     "textstream": ["src", "region"]}

    def startElement(self, name, attrs):
        aux = {}
        if name == "root-layout":
            for att in self.dicc[name]:
                aux[att] = attrs.get(att, "")
            self.list.append([name, aux])
        elif name == "region":
            for att in self.dicc[name]:
                aux[att] = attrs.get(att, "")
            self.list.append([name, aux])
        elif name == "img":
            for att in self.dicc[name]:
                aux[att] = attrs.get(att, "")
            self.list.append([name, aux])
        elif name == "audio":
            for att in self.dicc[name]:
                aux[att] = attrs.get(att, "")
            self.list.append([name, aux])
        elif name == "textstream":
            for att in self.dicc[name]:
                aux[att] = attrs.get(att, "")
            self.list.append([name, aux])

    def get_tags(self):
        return self.list

if __name__ == "__main__":
    print("programa principal")
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
