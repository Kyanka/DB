import uuid
from faker import Faker
from generator.utils import write_generated_data
from repo.movies_marks_repo import movies_marks_repo

faker = Faker()


def generate_movies_marks(movie_id, resource_id, quantity=10):
    movies_marks = []

    for i in range(quantity):
        # words_quantity = faker.random_int(1, 3)
        # words = faker.words(words_quantity)
        # name = ' '.join(words)

        movies_marks.append({
            '_id': f'{uuid.uuid4()}',
            'mark': faker.random_int(0, 10),
            'movie_id': movie_id,
            'resource_id': resource_id
        })

    write_generated_data(movies_marks_repo, movies_marks)
    return movies_marks
