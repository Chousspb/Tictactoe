from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from tictactoe.models import Game


def new_game(request: HttpRequest):
    new_game = Game()
    new_game.save()

    new_id = new_game.id
    response = redirect(f"/tic-tac/game/{new_id}")
    response.set_cookie("game_id", f"{new_id}")
    return response
