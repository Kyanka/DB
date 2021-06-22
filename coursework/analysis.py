import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from repo.movies_repo import movies_repo
from repo.directors_repo import directors_repo
from repo.resources_repo import resources_repo
from repo.movies_marks_repo import movies_marks_repo

graphics_path = 'results/graphics/'


def create_avarage_movie_mark():
    data = {}
    movies = movies_repo.find_all()

    for m in movies:
        movie_id = m['_id']
        movie_name = m['name']
        movie_marks = movies_marks_repo.get_movie_marks(movie_id)
        mean_value = np.mean(list(map(lambda m: m['mark'], movie_marks)))
        data[movie_name] = mean_value

    save_figure('average_movie_mark', lambda: plt.bar(data.keys(), data.values()))


def create_worst_movie_mark():
    data = {}
    movies = movies_repo.find_all()

    for m in movies:
        movie_id = m['_id']
        movie_name = m['name']
        movie_marks = movies_marks_repo.get_movie_marks(movie_id)
        min_value = np.nanmin(list(map(lambda m: m['mark'], movie_marks)))
        data[movie_name] = min_value

    save_figure('worst_movie_mark', lambda: plt.bar(data.keys(), data.values()))

def create_best_movie_mark():
    data = {}
    movies = movies_repo.find_all()

    for m in movies:
        movie_id = m['_id']
        movie_name = m['name']
        movie_marks = movies_marks_repo.get_movie_marks(movie_id)
        max_value = np.nanmax(list(map(lambda m: m['mark'], movie_marks)))
        data[movie_name] = max_value

    save_figure('best_movie_mark', lambda: plt.bar(data.keys(), data.values()))


def create_avarage_director_movies_marks(name):
    data = {}
    movies = movies_repo.find_movies_by_director(name)

    for m in movies:
        movie_id = m['_id']
        movie_name = m['name']
        movie_marks = movies_marks_repo.get_movie_marks(movie_id)
        mean_value = np.mean(list(map(lambda m: m['mark'], movie_marks)))
        data[movie_name] = mean_value

    save_figure('average_director_movies_marks', lambda: plt.bar(data.keys(), data.values()))


def save_figure(image_name, create_figure=None, plot=None):
    fig = plt.figure() if plot is None else plot.get_figure()
    fig.set_figwidth(14)
    if create_figure is not None:
        create_figure()
    fig.savefig(graphics_path + image_name + '.png', dpi=fig.dpi)
