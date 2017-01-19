#!/usr/bin/python

import argparse
import urllib2
from upsilon.serviceHelpers import *

parser = argparse.ArgumentParser();
parser.add_argument("baseurl")
parser.add_argument("-c", "--criticalCount", type = int, default = 0)
parser.add_argument("-w", "--warningCount", type = int, default = 5)
args = parser.parse_args()

import json

content = urllib2.urlopen(args.baseurl).read()
jsonStructure = json.decoder(content);

if len(jsonStructure) > args.countCritical:
    exitCritical()
elif len(jsonStructure) > args.countWarning:
    exitWarning()
else:
    exitOk()
