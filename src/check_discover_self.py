#!/usr/bin/python

from upsilon.service import ServiceController, easyexec

srv = ServiceController()

release, _ = easyexec(["cat", "/etc/redhat-release"])
srv.addSubresult("release", value = release)
srv.exitOk()
