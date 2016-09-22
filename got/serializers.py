from rest_framework import serializers
from got.models import Battles


class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battles
        field = ('id','name', 'year', 'battle_number', 'attacker_king', 'defender_king', 'attacker_outcome', 'bettle_type',
                 'major_death', 'major_capture', 'attacker_size', 'defender_size', 'attacker_commander', 'defender_commander',
                 'summer', 'location', 'region', 'note')
