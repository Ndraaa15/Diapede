from rest_framework import serializers
from .models import Diabetes

class DiabetesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diabetes
        fields = '__all__'