#!/usr/bin/python

from upsilon.service import ServiceController
from os import listdir
from os.path import join

powerSupplies = "/sys/class/power_supply/"

onAcPower = False
hasBattery = False
batteryCharge = 0

metadata = ServiceController()

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
	metadata.addMetric("batteryCharge", batteryCharge, karma)
	metadata.exit(karma, "On Battery, charge is: " + str(batteryCharge) + "%")
else:
	metadata.exitCritical("Can't detect power source!")
