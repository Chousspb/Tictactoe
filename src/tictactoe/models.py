from django.db import models
from django.db.models import Q
from itertools import chain

class Game(models.Model):
    size = models.IntegerField(default=3)
    winner = models.CharField(default=None, blank=True, null=True, max_length=10)
    current_item = models.CharField(max_length=5, default="cross")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def check_winner(self):
        winning_combinations = list(chain(
            [[(i, j) for j in range(self.size)] for i in range(self.size)],
            [[(i, j) for i in range(self.size)] for j in range(self.size)],
            [[(i, i) for i in range(self.size)]],
            [[(i, self.size - 1 - i) for i in range(self.size)]]
        ))

        for combination in winning_combinations:
            crosses = 0
            zeros = 0
            for coord in combination:
                step = self.step_set.filter(coord_x=coord[0], coord_y=coord[1]).first()
                if step:
                    if step.chosen == 'cross':
                        crosses += 1
                    elif step.chosen == 'zero':
                        zeros += 1

            if crosses == self.size:
                self.winner = 'Крестики'
                self.save()
                return
            elif zeros == self.size:
                self.winner = 'Нолики'
                self.save()
                return

    class Meta:
        db_table = "tictactoe_games"

class Step(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    coord_x = models.IntegerField(null=False)
    coord_y = models.IntegerField(null=False)
    chosen = models.CharField(max_length=5, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tictactoe_steps"
