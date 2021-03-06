# tplinkW215-maas-webhook-server

This is a very, very simple toy project to control power for a PC connected to a TPLINK W215 smartplug.
It uses a library called pyW215 to interface with the W215 plug, and flask to present a simple API.

Documentation about the MAAS webhook power driver is here:
https://maas.io/docs/snap/3.1/ui/power-management

Note that MAAS also sends the machine id in requests, so you could modify this to control multiple machines.

The "power_query" GET expects a response of the following:
{"power_state": "on|off|unknown"}

Running:
- Edit server.py and fill in your smart plug details (ip address and pin)
- run the server with python server.py
- test with POST and GET requests, the endpoints exposed are:
- http://x.x.x.x:1800/power_off/ (POST)
- http://x.x.x.x:1800/power_on/ (POST)
- http://x.x.x.x:1800/status/ (GET)
- Once verified, you should be able to configure a webhook power driver for machine in MAAS UI