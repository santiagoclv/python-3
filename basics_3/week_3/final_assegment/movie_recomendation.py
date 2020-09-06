from ..libs.requests_with_caching import get
from ..safe_get import safe_get

def get_movies_from_tastedive(movie_title):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {"limit": 5, "type": "movies"}
    params_diction["q"] = movie_title
    resp = get(baseurl, params = params_diction)
    return resp.json()

def extract_movie_titles(movies_data):
    return [ safe_get(movie, "Name") for movie in safe_get(movies_data, "Similar.Results") ]

def reduce(function, sequence, initial=None):
    it = iter(sequence)
    value = initial
    for element in it:
        value = function(value, element)
    return value

def get_related_titles(titles):
    movies_res = [ get_movies_from_tastedive(movie) for movie in titles]
    related_titles = reduce(lambda acc, li: acc + li,[extract_movie_titles(data) for data in movies_res], [])
    return list(set(related_titles))