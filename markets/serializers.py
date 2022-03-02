from rest_framework import serializers

from markets.models import Market


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'
        # fields = [
        #     'id', 'name', 'email', 'master',
        #     'reg_date', 'update_date',
        # ]
