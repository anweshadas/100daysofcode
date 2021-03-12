#!/usr/bin/env python3


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
        print("The input file does not exists. Enter a file as input that exists.")
        sys.exit(-1)
    if args.output:
        directory = args.output
        if not os.path.exists(directory):
            print("The output directory does not exists. Enter a directory as output that exists.")
        
    else:
        directory = "./"

    with open(filename) as fobj:
        for line in fobj:
            url = line.strip()
            r = httpx.get(url)
            if r.status_code != 200:
                print(f"Download error {url}")
                continue

            fname = url.split("/")[-1]
            fname = os.path.join(directory,fname)
            print(f"Downloading {fname}")
            try:
                with open(fname,"wb") as fobj:
                    fobj.write(r.read())
            except PermissionError:
                print("Can not write to the output director. Permission Error")
                sys.exit()



if __name__ == "__main__":
    main()