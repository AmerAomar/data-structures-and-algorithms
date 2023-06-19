# Comparator function for sorting movies by most recent year first
def sort_movies_by_year(movies):
    movies.sort(key=lambda movie: movie['year'], reverse=True)
    return movies

# Comparator function for sorting movies alphabetically by title, ignoring leading articles
def sort_movies_by_title(movies):
    articles = ['A', 'An', 'The']
    movies.sort(key=lambda movie: remove_articles(movie['title'], articles))
    return movies

# Helper function to remove leading articles from movie titles
def remove_articles(title, articles):
    words = title.split()
    if words[0] in articles:
        return ' '.join(words[1:])
    return title

# Sample data
movies = [
    {'title': 'The Avengers', 'year': 2012, 'genres': ['Action', 'Adventure', 'Sci-Fi']},
    {'title': 'A Beautiful Mind', 'year': 2001, 'genres': ['Biography', 'Drama']},
    {'title': 'Inception', 'year': 2010, 'genres': ['Action', 'Adventure', 'Sci-Fi']},
    {'title': 'Anchorman: The Legend of Ron Burgundy', 'year': 2004, 'genres': ['Comedy']},
]

# Sort movies by most recent year first
sorted_movies_by_year = sort_movies_by_year(movies)
print("Movies sorted by year:")
for movie in sorted_movies_by_year:
    print(movie['title'], movie['year'])

# Sort movies alphabetically by title, ignoring leading articles
sorted_movies_by_title = sort_movies_by_title(movies)
print("\nMovies sorted by title (ignoring leading articles):")
for movie in sorted_movies_by_title:
    print(movie['title'], movie['year'])
