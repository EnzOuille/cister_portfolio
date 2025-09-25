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

# Idées 

Actuellement, la recherche et les détails du film sont faits via omdb, la limitation est pour les titres français, le plus intéressant serait de récupérer les résultats globaux avec themoviedb
pour récup l'id du film souhaité et ensuite faire la recherche détaillée auprès de omdb pour obtenir les détails et les votes, c'est la façon la plus simple et la plus globale possible.

On pourrait également modifier le contenu pour que quand l'on ai pas d'images le contenu prenne toute la largeur. Ou alors on n'affiche pas les contenu sans images.

Ce serait bien d'ajouter un lien vers la fiche du film via l'id récup par themoviedb.

Les résultats doivent être supprimés après avoir sélectionné un film, sinon les anciens résultats sont encore présents même après plusieurs recherches.

Il faudrait harmoniser la page et la rendre plus belle, pour cela il faudrait arrondir l'ensemble, passer dans un fond coloré mais sobre, avec ptet des formes sur le côté de la page.

L'ajout d'un lien pour ajouter le film à sa playlist letterboxd serait aussi une bonne idée.
*By Enzo Cisternino*
