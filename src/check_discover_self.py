#!/usr/bin/python

from upsilon.serviceHelpers import *

metadata = clsmetadata()

release, _ = easyexec(["cat", "/etc/redhat-release"]);
metadata.addSubresult("release", value = release)

exit(metadata=metadata)
