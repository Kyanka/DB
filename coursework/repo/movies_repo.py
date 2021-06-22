import numpy as np
from repo.base_repo import BaseRepository
from db.connection import db
from repo.directors_repo import directors_repo


class MoviesRepository(BaseRepository):
    def __init__(self, collection):
        super().__init__(collection)

    def find_movies_by_director(self, director_name):
        director = directors_repo.find_director_by_name(director_name)
        for a in director:
            movies = self.find({'director_id': a['_id']})
        return movies

movies_repo = MoviesRepository(db['movies'])