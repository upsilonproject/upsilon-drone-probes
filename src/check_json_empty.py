#!/usr/bin/python

import argparse
import urllib2
from upsilon.serviceHelpers import *

parser = argparse.ArgumentParser();
parser.add_argument("baseurl")
parser.add_argument("-c", "--countCritical", type = int, default = 0)
parser.add_argument("-w", "--countWarning", type = int, default = 5)
args = parser.parse_args()

import json

content = urllib2.urlopen(args.baseurl).read()

try:
    jsonStructure = json.loads(content);
except: 
    print "Could not parse JSON"
    print content

    exitCritical()

if len(jsonStructure) > args.countCritical:
    exitCritical()
elif len(jsonStructure) > args.countWarning:
    exitWarning()
else:
    exitOk()
