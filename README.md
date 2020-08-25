# PBX Cloud Bridge

An easily maintainable bridge between voip handsets and a hosted pbx provider.

Throughout these documents we are assuming installation is on a server running Ubuntu 18.04

# Beta Version
It's still early days for the project and we're not at a working state just yet. Once we are, this tag will be removed.

# Limitations
* UDP only - need to add support for TCP and TLS
* Not handling DNS lookup of NTP hosts
* Handsets must be on the same SRTP setting for local direct calls to be successful

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
