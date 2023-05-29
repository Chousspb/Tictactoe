from django.http import HttpRequest
from django.shortcuts import render
from tictactoe.models import Game


def index(request: HttpRequest):
    if not request.COOKIES.get('game_id'):
        print('Can not find game_id cookie')
    title = "Список игр"
    context = {"page_title": title}

    games = Game.objects.all().order_by('-id')[:15]
    context['games'] = games
    response = render(request, 'tictactoe/templates/index.html', context)

    return response
