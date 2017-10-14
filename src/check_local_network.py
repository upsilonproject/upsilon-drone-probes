#!/usr/bin/python

from upsilon.serviceHelpers import *
from subprocess import Popen, PIPE
from argparse import ArgumentParser
import re

metadata = clsmetadata()

parser = ArgumentParser();
parser.add_argument("--network", required = True)
args = parser.parse_args()

p = Popen(["nmap", "-sn", args.network], stdout = PIPE, stderr = PIPE)
out, err = p.communicate()

hosts=[]
for line in re.findall("Nmap scan report for (.+)", out):
  metadata.addSubresult(line);

exit(metadata = metadata)
