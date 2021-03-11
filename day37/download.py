#!/usr/bin/env python3

import os 
import argparse
import httpx


parser = argparse.ArgumentParser()
parser.add_argument("--input", help="input filepath",
                    type=str, required=True)
args = parser.parse_args()

filename = args.input

with open(filename) as fobj:
    for line in fobj:
        url = line.strip()
        r = httpx.get(url)
        fname = url.split("/")[-1]
        print(f"downloading {fname}")
        with open(fname,"wb") as fobj:
            fobj.write(r.read())