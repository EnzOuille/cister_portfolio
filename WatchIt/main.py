# -*- coding: utf-8 -*-
import requests
import json

themoviedb_read_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MGFhZDdmMDczNzdhN2ZiNWMxOGU4MmY2NDBhYmI0YiIsIm5iZiI6MTc1NjkwNDc2Ni44MDE5OTk4LCJzdWIiOiI2OGI4M2QzZTVlMGQ0N2IwNzU4Y2Q3ZjYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.MC-nQ0bU-z-Rm3vfhEHEnLmQIyGQWWqqXX9masn82oI"

def user_loop():
    print("Bienvenue dans WatchIt?")
    do_we_stop = False
    while not do_we_stop:
        user_input = input("Saissisez un nom de film : ")
        print("Vous avez tapé : {}".format(user_input))
        user_input = input("Si vous voulez continuer, tapez 'oui' : ")
        if user_input != "oui":
            do_we_stop = True
    print("Sortie de l'application WatchIt?")

def themoviedb_auth():
    url = "https://api.themoviedb.org/3/authentication"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer {}".format(themoviedb_read_key)
    }

    response = requests.get(url, headers=headers)

    print(response.text)
    
def themoviedb_search_movie(movie_name):
    url = "https://api.themoviedb.org/3/search/movie"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer {}".format(themoviedb_read_key)
    }
    params = {
        "query": movie_name,
        "language": "fr-FR",
        "include_adult": True,
    }
    
    response = requests.get(url, params=params, headers=headers)
    json_response = json.loads(response.text)
    json_formatted_response = json.dumps(json_response["results"][0], indent=2)
    print(json_formatted_response.encode('utf-8').decode('unicode_escape'))
    
# user_loop()
# themoviedb_auth()
themoviedb_search_movie("Avengers")