from rest_framework import serializers

from markets.models import Market
from accounts.serialzers import UserSerializer


class MarketSerializer(serializers.ModelSerializer):
    master = UserSerializer(read_only=True)

    class Meta:
        model = Market
        fields = [
            'id', 'name', 'email', 'master',
            'reg_date', 'update_date',
        ]
