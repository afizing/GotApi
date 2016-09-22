from django.db import models


# Create your models here.
class Battles(models.Model):
    name = models.CharField(max_length=52)
    year = models.IntegerField()
    battle_number = models.IntegerField()
    attacker_king = models.CharField(max_length=24)
    defender_king = models.CharField(max_length=24)
    attacker_1 = models.CharField(max_length=27)
    attacker_2 = models.CharField(max_length=9)
    attacker_3 = models.CharField(max_length=7)
    attacker_4 = models.CharField(max_length=6)
    defender_1 = models.CharField(max_length=16)
    defender_2 = models.CharField(max_length=9)
    defender_3 = models.CharField(max_length=10)
    defender_4 = models.CharField(max_length=10)
    attacker_outcome = models.CharField(max_length=4)
    battle_type = models.CharField(max_length=14)
    major_death = models.CharField(max_length=1)
    major_capture = models.CharField(max_length=1)
    attacker_size = models.CharField(max_length=6)
    defender_size = models.CharField(max_length=5)
    attacker_commander = models.CharField(max_length=95)
    defender_commander = models.CharField(max_length=109)
    summer = models.CharField(max_length=1)
    location = models.CharField(max_length=36)
    region = models.CharField(max_length=15)
    note = models.CharField(max_length=257)

    def __str__(self):
        return self.name + "--" + str(self.year)