#!/usr/bin/python

from upsilon.service import ServiceController, easyexec
import datetime

srv = ServiceController()

release, _ = easyexec(["cat", "/etc/redhat-release"])
srv.addSubresult("release", value = release)
srv.addSubresult('date', value=str(datetime.datetime.now()))
srv.exitOk()
