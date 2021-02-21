#!/usr/bin/env python3

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def main():
    new_names = dedup_and_title_case_names(NAMES)
    print(new_names)
    surnames = sort_by_surname_desc(new_names)
    print(surnames)
    smallest_name = shortest_first_name(new_names)
    print(f" The smallest first name  is {smallest_name}")


def dedup_and_title_case_names(NAMES):
    """Should return a list of title cased names,
       each name appears only once"""

    names = list(dict.fromkeys(NAMES))
    new_names = [name.title() for name in names]
    return new_names


def sort_by_surname_desc(new_names):
    """Returns names list sorted desc by surname"""
    surnames = [name.split()[1] for name in new_names]
    surnames.sort(reverse = True)
    return surnames


def shortest_first_name(new_names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """

    spl_new_names = [name.split()[0] for name in new_names]
    smallest_len = len( spl_new_names[0])
    small_word = spl_new_names[0]

    for surname in spl_new_names:
        if len(surname) < smallest_len:
            small_word = surname
            smallest_len = len(surname)
    return small_word
        
if __name__ == "__main__":
        main()
