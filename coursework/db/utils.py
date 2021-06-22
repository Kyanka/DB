from repo.movies_repo import movies_repo
from repo.resources_repo import resources_repo
from repo.directors_repo import directors_repo
from repo.movies_marks_repo import movies_marks_repo
import json

backup_file = 'backup.json'


def drop():
    movies_repo.drop()
    resources_repo.drop()
    directors_repo.drop()
    movies_marks_repo.drop()


def backup():
    data = {
        'movies': movies_repo.find_all(),
        'directors': directors_repo.find_all(),
        'resources': resources_repo.find_all(),
        'movies_marks': movies_marks_repo.find_all(),
    }

    with open(backup_file, 'w+') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)


def restore():
    try:
        with open(backup_file, 'r+') as outfile:
            data = json.load(outfile)
            drop()
            movies_repo.insert_all(data['movies'])
            resources_repo.insert_all(data['resources'])
            directors_repo.insert_all(data['directors'])
            movies_marks_repo.insert_all(data['movies_marks'])
    except:
        print('File "backup.json" is not found or damaged\n')
