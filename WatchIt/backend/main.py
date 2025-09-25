from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI(title="Movie Info API")

# CORS pour autoriser ton frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # attention, juste pour dev local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TMDB_READ_KEY = os.getenv("TMDB_READ_KEY", "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MGFhZDdmMDczNzdhN2ZiNWMxOGU4MmY2NDBhYmI0YiIsIm5iZiI6MTc1NjkwNDc2Ni44MDE5OTk4LCJzdWIiOiI2OGI4M2QzZTVlMGQ0N2IwNzU4Y2Q3ZjYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.MC-nQ0bU-z-Rm3vfhEHEnLmQIyGQWWqqXX9masn82oI")
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w400"  # taille de l'image

OMDB_API_KEY= "f39685d4"
OMDB_API_URL = "http://www.omdbapi.com/"
@app.get("/search_tmdb")
def search_tmdb(movie_name: str = Query(..., description="Titre du film")):
    url = "https://api.themoviedb.org/3/search/movie"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_READ_KEY}"
    }
    params = {
        "query": movie_name,
        "language": "fr-FR",
        "include_adult": True,
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if "results" not in data or not data["results"]:
        return []

    # Retourne tous les films au format TomSelect + poster complet
    results = []
    for movie in data["results"]:
        print(movie)
        poster_url = TMDB_IMAGE_BASE + movie["poster_path"] if movie.get("poster_path") else ""
        results.append({
            "value": movie["title"],
            "text": f"{movie['title']} ({movie.get('release_date','')[:4]})",
            "poster": poster_url,
            "overview": movie.get("overview", ""),
            "vote_average": movie.get("vote_average", 0),
            "id": movie.get("id", "")
        })

    return results

@app.get("/search_omdb_tomselect")
def search_omdb_tomselect(movie_name: str = Query(..., description="Titre du film")):
    params = {
        "apikey": OMDB_API_KEY,
        "s": movie_name,
        "type": "movie",
        "r": "json"
    }
    
    response = requests.get(OMDB_API_URL, params=params)
    data = response.json()
    
    if "Search" not in data or not data["Search"]:
        return []
    
    results = []
    for movie in data["Search"]:
        print(movie)
        results.append({
            "value": movie["imdbID"],
            "text": movie["Title"],
            "poster": movie["Poster"]
        })
        
    return results

@app.get("/search_omdb_id")
def search_omdb_id(movie_id: str = Query(..., description="Id du film")):
    params = {
        "apikey": OMDB_API_KEY,
        "i": movie_id,
        "type": "movie",
        "r": "json"
    }
    
    response = requests.get(OMDB_API_URL, params=params)
    data = response.json()
    
    result = {
        "title": data.get("Title", ""),
        "year": data.get("Year", ""),
        "runtime": data.get("RunTime",""),
        "poster": data.get("Poster", ""),
        "ratings": data.get("Ratings", ""),
        "plot": data.get("Plot", "")
    }
    
    return result
    