from repo.base_repo import BaseRepository
from db.connection import db

resources_repo = BaseRepository(db['resources'])