from django.urls import path

from guess_game.views import game

urlpatterns = [
    path('', game.guess_game, name='guess_game')
]