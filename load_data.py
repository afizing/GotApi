import django

# Full path to your django project directory
your_djangoproject_home = r"C:\Users\Afizullah\PycharmProjects\Toppr\Toppr"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()

from got.models import Battles
import csv

# Full path and name to your csv file
csv_file_path="battles.csv"
dataReader = csv.reader(open(csv_file_path), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'name': # Ignore the header row, import everything
        battle = Battles()
        battle.name = row[0]
        battle.year = row[1]
        battle.battle_number = row[2]
        battle.attacker_king = row[3]
        battle.defender_king = row[4]
        battle.attacker_1 = row[5]
        battle.attacker_2 = row[6]
        battle.attacker_3 = row[7]
        battle.attacker_4 = row[8]
        battle.defender_1 = row[9]
        battle.defender_2 = row[10]
        battle.defender_3 = row[11]
        battle.defender_4 = row[12]
        battle.attacker_commander = row[13]
        battle.battle_type = row[14]
        battle.major_death = row[15]
        battle.attacker_size = row[16]
        battle.defender_size = row[17]
        battle.summer = row[18]
        battle.location = row[19]
        battle.region = row[20]
        battle.note = row[21]
        battle.save()
