# DNS Responder and Net Status Monitor

This process relies on the [Supervisor](http://supervisord.org/) to monitor and manage the Python script that is the DNS Responder.

You can place it anywhere you prefer on the server but it can run in situ once the repo is cloned. The file needs to be executable. Throughout this guide we will clone the repo into /opt and assume installation is on Ubuntu 18.04

The bridge requires a static IP address on the network. Consult your network admin on how to achieve this.

Let's update things and set the server timezone
```
sudo apt update
sudo apt upgrade

sudo dpkg-reconfigure tzdata
```

Install system requirements:
```
sudo apt install git python3-scapy supervisor
```

Clone the repo
```
sudo git -C /opt clone https://github.com/Siptalk/pbx-cloud-bridge.git
sudo chmod 0755 /opt/pbx-cloud-bridge/python/dnsresponder.py 
sudo chmod 0755 /opt/pbx-cloud-bridge/python/netstat-monitor.py 
```

Create a config dir in /etc
```
sudo mkdir /etc/cloudbridge
```

Copy the sample config file and modify as required for your setup
```
sudo cp /opt/pbx-cloud-bridge/python/sample.config.ini /etc/cloudbridge/dns-config.ini
```

Disable systemd-resolved and stop it from binding to port 53
```
sudo nano /etc/systemd/resolved.conf 
```
add or uncomment the following line
```
DNSStubListener=no
```
now disable it
```
sudo systemctl stop systemd-resolved.service
sudo systemctl disable systemd-resolved.service
```

Supervisor configuration:
```
sudo nano /etc/supervisor/conf.d/dnsresponder.conf
```
```
[program:dnsresponder]
command=/opt/pbx-cloud-bridge/python/dnsresponder.py
autostart=true
autorestart=true
stderr_logfile=/var/log/dnsresponder.err.log
stdout_logfile=/var/log/dnsresponder.out.log
```

```
sudo nano /etc/supervisor/conf.d/netstatmonitor.conf
```
```
[program:netstatmonitor]
command=/opt/pbx-cloud-bridge/python/netstat-monitor.py
autostart=true
autorestart=true
stderr_logfile=/var/log/netstatmonitor.err.log
stdout_logfile=/var/log/netstatmonitor.out.log
```

```
sudo supervisorctl reread
sudo supervisorctl update
```

Now on another machine you should be able to dig @your.new.server.ip and receive the address you set in the config
```
dig @192.168.0.123 google.com A
```

Setup the firewall if you haven't already done so.
[Firewall Configuration](firewall.md)
