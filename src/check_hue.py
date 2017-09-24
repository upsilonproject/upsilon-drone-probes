#!/usr/bin/python

from upsilon.serviceHelpers import *
from upsilon.http import *

metadata = clsmetadata()

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--user", required = True);
parser.add_argument("--host", required = True)
args = parser.parse_args();

client = getHttpClient(False, args.host)
content = getHttpContent(client, "/api/" + args.user);

blob = json.loads(content);

for index in blob["lights"]:
  light = blob["lights"][index]

  if light["state"]["on"]:
    karma = "GOOD"
    description = "ON"
  else:
    karma = "BAD"
    description = "OFF"

  metadata.addMetric(light["name"], description, karma)

exit(metadata=metadata);
