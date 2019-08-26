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

    for line in reader:
        pass
    
    metadata.addMetric("valueFromCsv", line[0])

exit(metadata = metadata)
