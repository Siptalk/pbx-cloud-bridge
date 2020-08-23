# Firewall

Let's configure [UFW](https://wiki.ubuntu.com/UncomplicatedFirewall) to only allow traffic from our local LAN range.

In this case we'll use 192.168.0.0/24

Make sure you're connected to the server from an address in this range, or you'll be locked out once the firewall is enabled.

Construct the firewall .. add any other options as required for your setup.
```
ufw default deny incoming
ufw default allow outgoing
ufw allow from 192.168.0.0/24
```

Enable the firewall .. this is where you could lock yourself out, check the above settings.
```
ufw enable
```
