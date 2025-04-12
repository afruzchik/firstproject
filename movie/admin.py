from django.contrib import admin
from .models import Movie



class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "date")
    list_filter = ("year", "date")
    fields = ("name", "year", "date")


admin.site.register(Movie, MovieAdmin)