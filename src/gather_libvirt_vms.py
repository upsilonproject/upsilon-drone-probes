#!/usr/bin/python

from upsilon.serviceHelpers import *
from subprocess import Popen, PIPE
from argparse import ArgumentParser
import re

metadata = clsmetadata()

parser = ArgumentParser();
args = parser.parse_args()


def getVirshList():
    p = Popen(["virsh", "list", "--all"], stdout = PIPE, stderr = PIPE)
    out, err = p.communicate()

    return out.strip().split("\n")[2:]

for line in getVirshList():
    m = re.search("([-\d]+)\s+(\S+)\s+(.+)", line)

    if len(m.groups()) != 3:
        print("Warning, unmatched line: ", line)

    if m.group(3) == "running":
        karma = "GOOD"
    else:
        karma = "BAD"

    metadata.addMetric(m.group(2), value = m.group(3), karma = karma);

exit(metadata = metadata)
