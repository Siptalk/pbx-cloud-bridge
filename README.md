# PBX Cloud Bridge

An easily maintainable bridge between voip handsets and a hosted pbx provider.

Throughout these documents we are assuming installation is on a server running Ubuntu 18.04

# Firewall
Firewall this server off to only allow access to your local LAN
[Firewall Setup](firewall.md)

# DNS Responder
The DNS Responder simply answers any request with the IP address supplied by the config.ini file.

This allows the bridge to save the extension locally and then forward the request of to its intended endpoint.

[DNS Responder Details](dnsresponder.md)
