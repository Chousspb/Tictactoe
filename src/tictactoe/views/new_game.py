from django.http import HttpRequest, HttpResponse
from tictactoe.models import Game
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser


@login_required
def new_game(request: HttpRequest):
    try:
        custom_user = CustomUser.objects.get(user=request.user)
    except CustomUser.DoesNotExist:
        custom_user = CustomUser(user=request.user)
        custom_user.save()

    new_game = Game()
    new_game.save()

    new_id = new_game.id
    response = redirect(f"/tic-tac/game/{new_id}")
    response.set_cookie("game_id", f"{new_id}")
    return response
