# Opensips SIP router
The main SIP packet handling is done with Opensips version 2.4

The standard Opensips config file needs to be updated with the file from the repo, please see below.

Install Opensips 2.4
```
sudo apt install gnupg

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 049AD65B

sudo echo "deb http://apt.opensips.org xenial 2.4-releases" >/etc/apt/sources.list.d/opensips.list 

sudo apt update
sudo apt install opensips
```

Assuming you have cloned the repo at this point, if not you can follow the instructions at [DNS Responder](dnsresponder.md)

Move the default config file and copy the new one into place
```
sudo mv /etc/opensips/opensips.cfg /etc/opensips/opensips.cfg_bak
sudo cp /opt/opensips/opensips.cfg /etc/opensips/opensips.cfg
```

We need to change the logging to feed into its own log file
```
sudo echo "local7.* /var/log/opensips.log\n" >> /etc/rsyslog.d/opensips.conf
```

Now restart syslog
```
sudo service rsyslog restart
```

Now restart Opensips
```
sudo systemctl restart opensips.service
```

At this point you should be able to update a handset dns with the bridge ip address and see the signalling traffic start routing via the bridge

```
sudo tail -f /var/log/opensips.log
```
