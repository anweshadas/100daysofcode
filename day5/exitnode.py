#!/usr/bin/env python3 

import ipinfo
import os
import json


def main():
    
    datafile = "/home/adas/code/100daysofcode/day5/torexitlist.txt"
    ips = get_ip(datafile)
    for ip_address in ips:
        write_ip(ip_address)

    
    
def get_ip(datafile): 
    ips = []
    with open(datafile) as fobj:
        for ip in fobj:
            ip = ip.strip()
            ips.append(ip)
    return ips

def write_ip(ip_address):
    print(ip_address)
    access_token = 'xxxx'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory,"torip", f'{ip_address}.json')

    with open(filename,"w") as fobj:
        json.dump(details.all,fobj)    

if __name__ == "__main__":
    main()