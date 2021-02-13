#!/usr/bin/env python3

# output
# 01. director_name          avarage score
#-----------------------------------------
# title_year] movie_title       imdb_score

# TODO
# get csv data
# read data 
# store info in a dictionary, k = director_name,v[]
# v = [avarage score, title_year, movie_title, imdb_score]
# calculate the avarage score 
# send the avarage score
# print the output 

import os
import csv
from collections import defaultdict
from collections import Counter
from pprint import pprint

def main():
    filename = get_csv_data()
    results = read_data(filename)
    average_of_director = count_avarage(results)
    average_of_director.sort(reverse=True)
    top_directors = average_of_director[0:19]
    pprint(top_directors)
    count = 1
    for average, director in top_directors:    
        print(f"{count:02d}. {director}\t\t{average:.2f}")
        print ("------------------------------------")
        movies = results[director]
        movies.sort(key=lambda movie: movie[1], reverse=True)
        for movie in movies:
            print(f"{movie[2]}] {movie[0]}\t\t{movie[1]:.2f}")
        count +=1
    
    
def get_csv_data():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory,'downloaded.csv' )
    return filename
    

def read_data(filename):
    results = defaultdict(list)
    filename = "/home/adas/code/100daysofcode/day7/downloaded.csv"
    with open(filename) as fobj:
        reader = csv.DictReader(fobj)
        line_count = 0    
        for row in reader:
            try:
                year = int(row['title_year'])
            except ValueError:
                print(row["title_year"])
            
            if year < 1960:
                continue
            m = (row['movie_title'],float(row['imdb_score']), year)
            results[row['director_name']].append(m)
            line_count += 1
        return results

def count_avarage(results):
    data = []
    for k,v in results.items():
        number_of_movies = 0
        total_score = 0
        for movie in v:
            number_of_movies += 1
            total_score += movie[1]
        if number_of_movies <= 4:
            continue
        #conuting average point of a director
        average = total_score / number_of_movies
        director_average = (average,k)
        data.append(director_average)
    return data


if __name__ == "__main__":
        main()