#!/usr/bin/python

from upsilon_common import *
from os import listdir
from os.path import join

powerSupplies = "/sys/class/power_supply/"

onAcPower = False
hasBattery = False
batteryCharge = 0

for supply in listdir(powerSupplies):
	if "AC" in supply and open(join(powerSupplies, supply, "online"), 'r').read().strip() == "1":
		onAcPower = True

	if "BAT" in supply:
		hasBattery = True

		batteryCharge = int(open(join(powerSupplies, supply, "capacity"), 'r').read().strip())

if onAcPower:
	exit(OK, None, "On AC Power")
elif hasBattery:
	karma = OK if batteryCharge > 25 else CRITICAL
	metadata = clsmetadata()
	metadata.addMetric("batteryCharge", batteryCharge, karma)
	exit(karma, metadata, "On Battery, charge is: " + str(batteryCharge) + "%")
else:
	exit(CRITICAL, None, "Can't detect power source!")
