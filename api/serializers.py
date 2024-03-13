from rest_framework import serializers
from .models import *

class MiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiningData
        fields = "__all__"
