from rest_framework import serializers
from .models import PlantedTree

class PlantedTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantedTree
        fields = ['id', 'plant', 'latitude', 'longiture', 'planted_at']
