#!/usr/bin/python

from upsilon.service import ServiceController, easyexec
from argparse import ArgumentParser
import re

srv = ServiceController()

parser = ArgumentParser();
args = parser.parse_args()

def getVirshList():
    stdout, stderr = easyexec(["virsh", "list", "--all"])

    return stdout.strip().split("\n")[2:]

for line in getVirshList():
    m = re.search("([-\d]+)\s+(\S+)\s+(.+)", line)

    if len(m.groups()) != 3:
        print("Warning, unmatched line: ", line)

    if m.group(3) == "running":
        karma = "GOOD"
    else:
        karma = "BAD"

    srv.addMetric(m.group(2), value = m.group(3), karma = karma);

srv.exitOk()
