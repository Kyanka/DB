from generator.generate_movies import generate_movies
from generator.generate_directors import generate_directors
from generator.generate_resources import generate_resources
from generator.generate_movies_marks import generate_movies_marks

def generate_all(directors_amount, movies_amount, resources_amount):
    directors = generate_directors(directors_amount)
    resources = generate_resources(resources_amount)
    all_movies = []

    for a in directors:
        movies = generate_movies(a['_id'], movies_amount)
        for m in movies:
            all_movies.append(m)

    for r in resources:
        for m in all_movies:
            movies_marks = generate_movies_marks(m['_id'], r['_id'], 1)