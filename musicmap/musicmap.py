#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from lxml import html, etree
import urllib.request as urllib

def parseArguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("artist", help = "Name of the Artist", type=str)
    parser.add_argument("-n", "--num", help="Amount of similar Artists", type=int, default=10)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parseArguments()
    root = html.parse(urllib.urlopen('https://www.music-map.com/' + args.artist.replace(" ", "+"))).getroot()
    artists_div = root.get_element_by_id("gnodMap")
    for i in range(1, args.num +1):
        print(artists_div[i].text)