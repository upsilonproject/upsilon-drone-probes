#!/usr/bin/python

from upsilon.serviceHelpers import *

metadata = clsmetadata()
metadata.addSubresult("testing", comment = "testing")

exit(metadata=metadata)
