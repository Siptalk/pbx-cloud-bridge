#!/usr/bin/python3

from scapy.all import DNS, DNSRR
import socket, os, configparser

dirname  = os.path.dirname(__file__)
cfg_path = os.path.join(dirname, 'config.ini')
config   = configparser.ConfigParser()
config.read(cfg_path)

HOST 	= config.get('DNS','HOST')
PORT 	= config.getint('DNS','PORT')
IPv4IP 	= config.get('DNS','IPv4IP')
IPv6IP 	= config.get('DNS','IPv6IP')
TTL 	= config.getint('DNS','TTL')

udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udps.bind((HOST,PORT))
try:
	while 1:
		data, addr = udps.recvfrom(1024)
		# decode the DNS data
		decoded = DNS(data)
		qtype = "A"
		respip = IPv4IP

# ipv6 capability pending ..
#		qtype = decoded["DNS"].qd.qtype
#		if qtype == "AAAA":
#			respip = IPv6IP
#		else:
#			respip = IPv4IP

		# build a response
		resp = DNS(id=decoded["DNS"].id,ancount=1, qr=1, an=DNSRR(type=qtype,ttl=TTL,rdata=respip,rrname=decoded["DNS"].qd.qname))
		# send the response
		udps.sendto(bytes(resp), addr)

except KeyboardInterrupt:
	udps.close()

