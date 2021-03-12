#!/usr/bin/env python3

# r = anything other than 200 is error
# wrong input filepath 
# wrong output directory - 

import os 
import argparse
import httpx
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input filepath",
                        type=str, required=True)
    parser.add_argument("--output", help="output directory",
                        type=str)                        
    
    args = parser.parse_args()

    filename = args.input
    if not os.path.exists(filename):
        print("The input file does not exist. Enter a file as input that exists.")
        sys.exit(-1)
    if args.output:
        directory = args.output
    else:
        directory = "./"

    with open(filename) as fobj:
        for line in fobj:
            url = line.strip()
            r = httpx.get(url)
            fname = url.split("/")[-1]
            fname = os.path.join(directory,fname)
            print(f"Downloading {fname}")
            with open(fname,"wb") as fobj:
                fobj.write(r.read())

if __name__ == "__main__":
    main()