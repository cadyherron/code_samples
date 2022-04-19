"""
Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes)
    and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
"""


def movie_picker(flight_length, movie_lengths):
    sorted_lengths = sorted(movie_lengths)
    right_index = len(movie_lengths) - 1
    for movie_length in movie_lengths:
        if movie_length + movie_lengths[right_index] == flight_length:
            return True
        elif movie_length + movie_lengths[right_index] > flight_length:
            return False
        else:
            right_index -= 1

    return False


def two_movies(movie_lengths, flight_length):
    movie_lengths_seen = set()
    for first_movie_length in movie_lengths:
        matching_second_movie = flight_length - first_movie_length
        if matching_second_movie in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    return False
