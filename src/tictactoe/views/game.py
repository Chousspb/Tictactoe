from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from tictactoe.models import Game, Step


def check_winner(game: Game, coord_x: int, coord_y: int) -> str:
    # Проверка по горизонтали
    row_steps = Step.objects.filter(game=game, coord_x=coord_x).order_by("coord_y")
    row_chosen = [step.chosen for step in row_steps]
    if len(set(row_chosen)) == 1:
        return row_chosen[0]

    # Проверка по вертикали
    col_steps = Step.objects.filter(game=game, coord_y=coord_y).order_by("coord_x")
    col_chosen = [step.chosen for step in col_steps]
    if len(set(col_chosen)) == 1:
        return col_chosen[0]

    # Проверка по первой диагонали
    if coord_x == coord_y:
        diagonal_1_steps = Step.objects.filter(game=game, coord_x=coord_y, coord_y=coord_x).order_by("coord_x")
        diagonal_1_chosen = [step.chosen for step in diagonal_1_steps]
        if len(set(diagonal_1_chosen)) == 1:
            return diagonal_1_chosen[0]

    # Проверка по второй диагонали
    if coord_x == game.size - 1 - coord_y:
        diagonal_2_steps = Step.objects.filter(game=game, coord_x=coord_x, coord_y=game.size - 1 - coord_y).order_by("coord_x")
        diagonal_2_chosen = [step.chosen for step in diagonal_2_steps]
        if len(set(diagonal_2_chosen)) == 1:
            return diagonal_2_chosen[0]

    return ""

def game(request: HttpRequest, game_id: int):
    form_error = {'radio_missed': ""}
    choose = None
    item_type = None

    if request.method == "POST":
        game_id = int(request.POST['game_id'])
        item_type = request.POST['item_type']
        choose = request.POST.get('radio-choose')
        if not choose:
            form_error['radio_missed'] = "Нужно выбрать хоть что-то"
        else:
            coord_x, coord_y = choose.split(':')
            game = Game.objects.get(pk=game_id)

            if not game.winner:
                new_step = Step(game=game, coord_x=coord_x, coord_y=coord_y, chosen=item_type)
                new_step.save()

                game.current_item = 'zero' if item_type == 'cross' else 'cross'
                game.check_winner()

                game.save()

            return redirect(request.path)

    game = Game.objects.get(pk=game_id)
    steps = Step.objects.filter(game=game).all()

    # generating table
    rows = []
    for row in range(0, game.size):
        rows.append(
            [{"cell": f"{row}:{col}", "is_active": True} for col in range(game.size)]
        )
    if steps:
        for step in steps:
            rows[step.coord_x][step.coord_y]["is_active"] = False
            rows[step.coord_x][step.coord_y]["chosen"] = "X" if step.chosen == "cross" else "O"

    context = {
        "form_error": form_error,
        "game_id": game_id,
        "item_string": "Крестики" if game.current_item == "cross" else "Нолики",
        "item_type": game.current_item,
        "rows": rows,
        "winner": game.winner
    }

    return render(request, "tictactoe/templates/game.html", context=context)

