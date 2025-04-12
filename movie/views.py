
from django.shortcuts import render

from movie.models import Movie


def home(requests):
    movie = Movie.objects.all()
    context = {
        "movie": movie
    }
    return  render(requests, "index.html", context)