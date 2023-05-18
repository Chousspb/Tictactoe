from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    if not request.COOKIES.get('game_id'):
        print('Can not find game_id cookie')
    return render(request, 'tictactoe/templates/index.html')