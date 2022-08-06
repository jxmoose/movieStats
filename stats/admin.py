from django.contrib import admin
from stats.models import Directors, Writers, Movie, Cast, Genres
# Register your models here.
admin.site.register(Directors)
admin.site.register(Movie)
admin.site.register(Writers)
admin.site.register(Cast)
admin.site.register(Genres)