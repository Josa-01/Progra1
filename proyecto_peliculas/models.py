class Movie:
    def __init__(self, data):
        self.id = data.get("id")
        self.title = data.get("title") or data.get("name")
        self.overview = data.get("overview")
        self.release_date = data.get("release_date") or data.get("first_air_date")
        self.poster_path = data.get("poster_path")
        self.vote_average = data.get("vote_average")
        self.genres = data.get("genres", [])
    
    def get_full_poster_url(self):
        if self.poster_path:
            return f"https://image.tmdb.org/t/p/w500{self.poster_path}"
        return ""
    
    def get_release_year(self):
        if self.release_date:
            return self.release_date.split("-")[0]
        return "N/A"
