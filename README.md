# PBX Cloud Bridge

An easily maintainable bridge between voip handsets and a hosted pbx provider.

Throughout these documents we are assuming installation is on a server running Ubuntu 18.04

# Limitations
* UDP only - need to add support for TCP and TLS
* Not handling DNS lookup of NTP hosts
* Handsets must be on the same SRTP setting for local direct calls to be successful

# Configuration Requirements
* set /etc/cloudbridge/opensips-listen.conf to your server ip
* set /etc/cloudbridge/dns-conf.ini IPv4IP variable to your server ip


# Firewall
Firewall this server off to only allow access to your local LAN
[Firewall Setup](firewall.md)

# DNS Responder
The DNS Responder simply answers any request with the IP address supplied by the config.ini file.

This allows the bridge to save the extension locally and then forward the request of to its intended endpoint.

[DNS Responder Details](dnsresponder.md)

# Opensips SIP Router
The Opensips SIP Router is the primary process that handles the signalling packets for the bridge.

[Opensips SIP Router](opensips.md)
