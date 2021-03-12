#!/usr/bin/env python3

import os 
import argparse
import httpx


def main():
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
            print(f"Downloading {fname}")
            with open(fname,"wb") as fobj:
                fobj.write(r.read())

if __name__ == "__main__":
    main()