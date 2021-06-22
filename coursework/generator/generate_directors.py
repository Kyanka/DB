import uuid
from faker import Faker
from generator.utils import write_generated_data
from repo.directors_repo import directors_repo

faker = Faker()


def generate_directors(quantity=10):
    directors = []

    for i in range(quantity):

        directors.append({
            '_id': f'{uuid.uuid4()}',
            'name': faker.name(),
        })
        
    write_generated_data(directors_repo, directors)
    return directors