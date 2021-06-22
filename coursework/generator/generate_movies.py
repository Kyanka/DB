import uuid
from faker import Faker
from generator.utils import write_generated_data
from repo.movies_repo import movies_repo

faker = Faker()


def generate_movies(director_id, quantity=10):
    movies = []

    for i in range(quantity):
        words_quantity = faker.random_int(1, 3)
        words = faker.words(words_quantity)
        name = ' '.join(words)
        movies.append({
            '_id': f'{uuid.uuid4()}',
            'name': name,
            'director_id': director_id,
        })

    write_generated_data(movies_repo, movies)
    return movies
