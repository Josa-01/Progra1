from flask import Flask, render_template, request
from tmdb_client import TMDB_API_Client
from models import Movie

app = Flask(__name__)
tmdb = TMDB_API_Client()

@app.route("/")
def index():
    movies_data = tmdb.get_popular_movies()
    movies = [Movie(m) for m in movies_data]
    return render_template("index.html", movies=movies)

@app.route("/search")
def search():
    query = request.args.get("q")
    movies = []
    if query:
        movies_data = tmdb.search_movies(query)
        movies = [Movie(m) for m in movies_data]
    return render_template("search_results.html", movies=movies, query=query)

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    movie_data = tmdb.get_movie_details(movie_id)
    movie = Movie(movie_data)
    return render_template("movie_details.html", movie=movie)

if __name__ == "__main__":
    app.run(debug=True)
