import pytest
from Sorting.movies import sort_movies_by_year, sort_movies_by_title

@pytest.fixture
def sample_movies():
    return [
        {'title': 'The Avengers', 'year': 2012, 'genres': ['Action', 'Adventure', 'Sci-Fi']},
        {'title': 'A Beautiful Mind', 'year': 2001, 'genres': ['Biography', 'Drama']},
        {'title': 'Inception', 'year': 2010, 'genres': ['Action', 'Adventure', 'Sci-Fi']},
        {'title': 'Anchorman: The Legend of Ron Burgundy', 'year': 2004, 'genres': ['Comedy']},
    ]

def test_sort_movies_by_year(sample_movies):
    sorted_movies = sort_movies_by_year(sample_movies)
    assert sorted_movies[0]['year'] >= sorted_movies[1]['year']
    assert sorted_movies[1]['year'] >= sorted_movies[2]['year']
    assert sorted_movies[2]['year'] >= sorted_movies[3]['year']

def test_sort_movies_by_title(sample_movies):
    sorted_movies = sort_movies_by_title(sample_movies)
    assert sorted_movies[0]['title'] == 'Anchorman: The Legend of Ron Burgundy'
    assert sorted_movies[1]['title'] == 'The Avengers'
    assert sorted_movies[2]['title'] == 'A Beautiful Mind'
    assert sorted_movies[3]['title'] == 'Inception'

