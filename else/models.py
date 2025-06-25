from django.db import models

# Create your models here.
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)

class Game(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='games_as_player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='games_as_player2')
    round_number = models.IntegerField(default=1)
    result = models.CharField(max_length=20, null=True, blank=True)  # "player1_win", "draw", etc.
    timestamp = models.DateTimeField(auto_now_add=True)

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    rock = models.IntegerField()
    paper = models.IntegerField()
    scissors = models.IntegerField()
    selected_move = models.CharField(max_length=10, null=True, blank=True)  # "rock", etc.

class Visitor(models.Model):
    ipaddress = models.CharField(max_length=50)
    useragent = models.CharField(max_length=100)
    acceptedlanguage = models.CharField(max_length=50, null=True)
    acceptedencoding = models.CharField(max_length=50, null=True)