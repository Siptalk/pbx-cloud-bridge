#!/usr/bin/python3

import os,time

hostname0 = "1.1.1.1"
hostname1 = "8.8.8.8"
filename = "/tmp/cloudbridge-netstat"
sleepsec = 30

try:
	while 1:
		response0 = os.system("ping -c 1 " + hostname0)
		response1 = os.system("ping -c 1 " + hostname1)

		if(response0 == 0 or response1 == 0):
			print("net is up")
			# one of the endpoints responded so the net is up
			if os.path.isfile(filename) and os.access(filename, os.R_OK):
				os.remove(filename)
		else:
			print("net is down")
			# there was no response so mark the net as offline
			f = open(filename, "w")
			f.write("offline")
			f.close()

		time.sleep(sleepsec)

except KeyboardInterrupt:
	print("end")


