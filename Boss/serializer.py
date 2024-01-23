from rest_framework import serializers
from Boss.models import Boss


class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
        fields = '__all__'
