from django.contrib import admin
from .models import Genero, Plataforma, Jogo, Review

admin.site.register(Genero)
admin.site.register(Plataforma)
admin.site.register(Jogo)
admin.site.register(Review)