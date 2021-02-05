#!/usr/bin/env python3

import os
import httpx
import csv
from collections import defaultdict
from collections import namedtuple
from collections import Counter
from pprint import pprint

Movie = namedtuple("Movie",["title", "score", "year"])

# This is code solves the same problem as movie.py

def main():
    filename = get_csv_data()
    directors = get_movies_by_director(filename)
    print(directors)
    cnt = count_directors(directors)
    print(cnt.most_common(5))

def get_csv_data():
    r = httpx.get("https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv")
    url_content = r.content
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory,'downloaded.csv' )
    with open(filename, 'wb') as fobj:
        fobj.write(url_content)
    return filename

def get_movies_by_director(data):
    directors = defaultdict(list)
    with open(data) as fobj:
        for line in csv.DictReader(fobj):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace("\xa0", "")
                year = int(line["title_year"])
                score = float(line["imdb_score"])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
            
        return directors 

def count_directors(directors):

    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies)
    return cnt

if __name__ == "__main__":
    main()
    