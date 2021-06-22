import numpy as np
from repo.base_repo import BaseRepository
from db.connection import db
class DirectorsRepository(BaseRepository):
    def __init__(self, collection):
        super().__init__(collection)

    def find_director_by_name(self, name):
        director = self.find({'name': name})
        return director

directors_repo = DirectorsRepository(db['directors'])