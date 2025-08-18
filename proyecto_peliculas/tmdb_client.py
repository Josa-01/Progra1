import requests
from config import API_KEY, BASE_URL

class TMDB_API_Client:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
    
    def get_popular_movies(self):
        url = f"{self.base_url}/movie/popular?api_key={self.api_key}&language=es"
        r = requests.get(url)
        return r.json().get("results", [])
    
    def search_movies(self, query):
        url = f"{self.base_url}/search/movie?api_key={self.api_key}&language=es&query={query}"
        r = requests.get(url)
        return r.json().get("results", [])
    
    def get_movie_details(self, movie_id):
        url = f"{self.base_url}/movie/{movie_id}?api_key={self.api_key}&language=es"
        r = requests.get(url)
        return r.json()
