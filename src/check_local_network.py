#!/usr/bin/python

from upsilon.service import ServiceController, easyexec
from subprocess import Popen, PIPE
from argparse import ArgumentParser
import re

srv = ServiceController()

parser = ArgumentParser();
parser.add_argument("--network", required = True)
args = parser.parse_args()


stdout, stderr = easyexec(["nmap", "-sn", args.network])

hosts=[]
for line in re.findall("Nmap scan report for (.+)", stdout):
  srv.addSubresult(line);

srv.exitOk()
