import numpy as np
from repo.base_repo import BaseRepository
from db.connection import db
from repo.movies_repo import movies_repo


class MoviesMarksRepository(BaseRepository):
    def __init__(self, collection):
        super().__init__(collection)

    def get_movie_marks(self, movie_id):
        marks = []
        movies = movies_repo.find({'_id': movie_id})
        
        for m in movies:
            movie_marks = self.find({'movie_id': m['_id']})
            marks = np.append(marks, movie_marks)
        
        return marks

movies_marks_repo = MoviesMarksRepository(db['movies_marks'])