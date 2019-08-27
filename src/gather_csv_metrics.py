#!/usr/bin/python

from upsilon.serviceHelpers import *
from argparse import ArgumentParser
import csv

parser = ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args();

metadata = clsmetadata();

with open(args.filename) as csvfile:
    reader = csv.reader(csvfile)

    lines = []

    for line in reader:
        lines.append(line)

    headers = lines[0:1][0]
    recentValues = lines[-1:][0]

    for index in range(len(headers)):
        metadata.addMetric(headers[index].strip(), recentValues[index].strip())


exit(metadata = metadata)
