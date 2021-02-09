#!/usr/bin/env python3 

# read all the json files in ./day5/torip/
# find out the value of country_name" of each ip
# count the how many has same value

import os
import json
from collections import namedtuple
from collections import Counter
from pprint import pprint

def main():

    directory = os.path.dirname(__file__)
    path = os.path.join(directory,"torip")
    data = read_json(path)
    countries = count_country(data)
    pprint(countries)
    
def read_json(path):

    results = []
    allfiles = os.listdir(path)
    for file in allfiles:
        if not file.endswith(".json"):
            continue
        filepath = os.path.join(path,file)
        with open(filepath) as fobj: 
            data = json.load(fobj)
            results.append(data)
            
    return results


def count_country(data):
    country_name = []
    cnt = Counter()
    for node in data:
        word = node["country_name"]
        cnt[word] += 1      
    return cnt


if __name__ == "__main__":
    #data = main()
    main()