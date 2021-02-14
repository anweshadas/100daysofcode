#!/usr/bin/env python3

# Todo
# Parse the downloaded unsorted dict and :
# Print out the 10th item in each.
# Print out the 45th key in the dictionary.
# Print out the 27th value in the dictionary.

import os
from pprint import pprint
from unsorteddictlist import *

def main():
    print(f"The 10th item of the list : {states_list[9]}.")
    tenth_item_dict =  parse_dict()
    print()

    
def parse_dict():
    count = 0
    for k,v in us_state_abbrev.items():
        if count == 10:
            print(f"The 10th item of the dictionary : {k,v}.")
        if count == 27:
            print(f"the 45th key in the dictionary:{v}")
        if count == 45:
            print(f"the 45th key in the dictionary:{k}")
        count += 1

        
    if __name__ == "__main__":
    main()