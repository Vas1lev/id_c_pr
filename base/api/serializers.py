from rest_framework import serializers
from base.models import Description, Info


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']
        model = Description


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Info

