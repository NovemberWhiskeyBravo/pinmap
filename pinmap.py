#!/usr/bin/env python
import nmap, json, time

json_data = open("config.json").read()
config = json.loads(json_data)

nm = nmap.PortScanner()

while True:
    nm.scan(arguments='-v -iR 1 -sV')

    for host in nm.all_hosts():
        if nm[host].state() == "down":
            print("[] - "+str(host)+" - target is down" )
        else:
            print("[] - "+str(host)+" - target is up" )
            f = open(config['outputFolder']+"/"+str(host)+".json","a+")
            f.write(str(nm[host]))
            f.close()
    time.sleep(config['restTime'])
