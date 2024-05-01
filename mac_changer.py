#!/usr/bin/env/python

interface=input("interface:>(eth0/wlan0)")
newmac=input("new mac:>")


import subprocess
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig"])
