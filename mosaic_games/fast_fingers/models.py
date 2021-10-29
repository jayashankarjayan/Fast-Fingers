import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GameData(models.Model):
    """docstring for GameData."""

    class Meta:
        permissions = [
        ("can_play_game", "Can play the game")
        ]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field="id", db_column="user_id")
    assinged_input = models.TextField(null=True)
    user_input = models.TextField()
    score = models.IntegerField(default=0)
    start_time = models.TimeField(default=datetime.datetime.now().time())
    end_time = models.TimeField(null=True)
