from .models import Permohonan
from rest_framework import serializers

class PermohonanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Permohonan
    fields = '__all__'