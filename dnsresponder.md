# DNS Responder

This process relies on the [Supervisor](http://supervisord.org/) to monitor and manage the Python script that is the DNS Responder.

You can place it anywhere you prefer on the server but it can run in situ once the repo is cloned. The file needs to be executable. Throughout this guide we will clone the repo into /opt and assume installation is on Ubuntu 18.04

The bridge requires a static IP address on the network. Consult your network admin on how to achieve this.

Let's update things and set the server timezone
```
sudo apt update
sudo apt upgrade

dpkg-reconfigure tzdata
```

Install system requirements:
```
sudo apt install git python3-scapy supervisor
```

Clone the repo
```
sudo git -C /opt clone https://github.com/Siptalk/pbx-cloud-bridge.git
sudo chmod 0755 /opt/pbx-cloud-bridge/python/dnsresponder.py 
```

Copy the sample config file and modify as required for your setup
```
sudo cp /opt/pbx-cloud-bridge/python/sample.config.ini /opt/pbx-cloud-bridge/python/config.ini
```

Disable systemd-resolved and stop it from binding to port 53
```
nano /etc/systemd/resolved.conf 
```
add or uncomment the following line
```
DNSStubListener=no
```
now disable it
```
systemctl stop systemd-resolved.service
systemctl disable systemd-resolved.service
```

Supervisor configuration:
```nano /etc/supervisor/conf.d/dnsresponder.conf```

```
[program:dnsresponder]
command=/opt/pbx-cloud-bridge/python/dnsresponder.py
autostart=true
autorestart=true
stderr_logfile=/var/log/dnsresponder.err.log
stdout_logfile=/var/log/dnsresponder.out.log
```

```
supervisorctl reread
supervisorctl update
```

Setup the firewall if you haven't already done so.
[Firewall Configuration](firewall.md)
