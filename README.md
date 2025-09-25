# WatchIt?

Le but de ce projet est de créer au fur et à mesure une application qui permet à partir d'un input textuel, permet d'obtenir des informations sur un film et d'avoir un croisement de notes, permettant de savoir si le film a reçu des critiques positives ou non.

# Lancement

```
cd backend
py -m pip install -r requirements.txt
py -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

# Fonctionnalités

- Trouver un film à partir de son nom
- Avoir le synopsis / poster / titre du film
- Avoir la note du film (TheMovieDb)
- Avoir une note croisée (TheMovieDb + IMDB + LetterboxD)

*By Enzo Cisternino*