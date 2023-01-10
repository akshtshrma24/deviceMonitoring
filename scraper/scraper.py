import time
import json

from prometheus_client import start_http_server, Gauge

from checkStatus import *


jsonFile = open("config.json")
js = json.load(jsonFile)


gauge = Gauge("is_up", "Is this IP/Name up", ['name', 'ip'])


ip_name_dict = {}
for name in js["IPS"]:
    ip_name_dict[name] = js["IPS"][name]
    gauge.labels(name, js["IPS"][name]).set(str(time.time()))


# start scraper
start_http_server(5002)
while (True):
    for name in ip_name_dict:
        ip_address = ip_name_dict[name]
        if (is_up(ip_address)):
            gauge.labels(name, ip_address).set(str(time.time()))
        time.sleep(40)
