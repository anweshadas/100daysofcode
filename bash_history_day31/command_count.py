#!/usr/bin/env python3

import os
from collections import Counter
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top",type =int, default=5)
    args = parser.parse_args()
    filename = get_filename()
    data = get_data(filename)
    command_counts = count_commands(data)
    #print(command_counts)
    most_common_commands = Counter(data).most_common(args.top)
    for t in most_common_commands:
        print(f"{t[0]} = {t[1]}")


def get_filename():
    directory = os.path.expanduser("~")
    filename = os.path.join(directory, '.bash_history')

    return filename

def get_data(filename):
    data = []
    with open(filename) as fobj:
        da = fobj.readlines()
        for com in da:
            data.append(com.strip())
    return data

def count_commands(data):
    cnt = Counter()
    for com in data:
        cnt[com] += 1
    return cnt


if __name__ == "__main__":
    main()


