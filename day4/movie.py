#!/usr/bin/env python3

# download the data set
# convert it into a defaultdict, k= directorname, v=nammedtuple(movienames)
# find out the 1directors with most amount of movies 

import os
import httpx
import csv
from collections import defaultdict
from collections import namedtuple
from collections import Counter
from pprint import pprint

Movie = namedtuple("Movie",["title", "score", "year"])

def main():
    #get_csv_data()
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory,'downloaded.csv' )
    results = read_data(filename)
    return results
    

def get_csv_data():
    r = httpx.get("https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv")
    url_content = r.content
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory,'downloaded.csv' )
    with open(filename, 'wb') as fobj:
        fobj.write(url_content)

def read_data(filename):
    results = defaultdict(list)
    with open(filename) as fobj:
        csv_reader = csv.DictReader(fobj)
        line_count = 0
        for row in csv_reader:
            try:
                year = int(row['title_year'])
            except ValueError:
                print(row["title_year"])

            if year < 1960:
                continue
            m = Movie(row['movie_title'],float(row['imdb_score']), year)
            results[row['director_name']].append(m)
            line_count += 1
        return results

 
    
if __name__ == "__main__":
    results = main()