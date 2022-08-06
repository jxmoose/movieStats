from xmlrpc.client import DateTime
import requests
import time
import uuid
from stats.models import Directors, Writers, Movie, Cast, Genres
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, render

#for processing data
def process(movie_list):
    date_column, rating_column = None, None
    acceptable_headers = ["Title", "Name", "Date", "Date Rated", "Your Rating", "Rating", "Const", ]
    for i in range(len(movie_list[0])):
        if "Rating" in movie_list[0][i]:
            rating_column = i
        elif "Date" in movie_list[0][i]:
            date_column = i
        elif movie_list[0][i] == "Name" or movie_list[0][i] == "Title":
            name_column = i
    uuid_user_id = uuid.uuid4()
    for i in range(1, len(movie_list)):
        name = movie_list[i][name_column]
        url = f'https://imdb-api.com/API/Search/k_nvwbbfzq/{name}'
        response = requests.get(url)
        movie_tconst = response.json()["results"][0]["id"]
        url = f'https://imdb-api.com/en/API/Title/k_nvwbbfzq/{movie_tconst}'
        response = requests.get(url).json()
        #for movie model
        imdb_rating = response["imDbRating"]
        votes = int(response["imDbRatingVotes"])
        release_date = response["releaseDate"]
        movie_title = response["title"]
        movie_rating = None if rating_column is None else movie_list[i][rating_column]
        date = None if date_column is None else movie_list[i][date_column]
        m = Movie.objects.create(imdbRating = imdb_rating, user_id = uuid_user_id, tconst = movie_tconst, title = movie_title, rating = movie_rating, releaseDate = release_date, watchDate = date, numVotes = votes)
        m.save()
        #for directors list
        for movie_director in response["directorList"]:
            d = Directors.objects.create(tconst = movie_tconst, director = movie_director["name"])
            d.save()

        #for writers list
        for movie_writer in response["writerList"]:
            w = Writers.objects.create(tconst = movie_tconst, writer = movie_writer["name"])
            w.save()

        #for genres list
        for movie_genre in response["genreList"]:
            g = Genres.objects.create(tconst = movie_tconst, genre = movie_genre["key"])
            g.save()
        
        #for cast list
        for movie_cast in response["starList"]:
            c = Cast.objects.create(tconst = movie_tconst, actor = movie_cast["name"])
        
        print(i)
