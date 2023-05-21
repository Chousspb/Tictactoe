from django.urls import path
from tictactoe.views import index, new_game, game

tic_tac_urlpatterns = [
    path('', index, name='index'),
    path("create-new-game", new_game),
    path("game/<int:game_id>", game),
    path('new_game/', new_game, name='new_game')
]
