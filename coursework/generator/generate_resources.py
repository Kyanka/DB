import uuid
from faker import Faker
from generator.utils import write_generated_data
from repo.resources_repo import resources_repo

faker = Faker()


def generate_resources(quantity=10):
    resources = []

    for i in range(quantity):
        words_quantity = faker.random_int(1, 3)
        words = faker.words(words_quantity)
        name = ' '.join(words)

        resources.append({
            '_id': f'{uuid.uuid4()}',
            'resource_name': name,
        })

    write_generated_data(resources_repo, resources)
    return resources