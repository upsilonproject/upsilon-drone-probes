#!/usr/bin/python

import argparse
import urllib3
from upsilon.service import ServiceController

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
    print("Could not parse JSON")
    print(content)

    exitCritical()

srv = ServiceController()

for thing in jsonStructure:
    title = "untitled"

    for key in ["name", "title"]:
      if key in thing:
          title = thing[key]
       
    srv.addSubresult(title, karma = "WARNING")

message = str(len(jsonStructure)) + " items in the list"

if len(jsonStructure) > args.countCritical:
    srv.exitCritical(message)
elif len(jsonStructure) > args.countWarning:
    srv.exitWarning(message)
else:
    exitOk()
