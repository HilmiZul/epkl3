from rest_framework import serializers
from .models import Siswa, Instansi

class SiswaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Siswa
    fields = '__all__'


class InstansiSerializer(serializers.ModelSerializer):
  class Meta:
    model = Instansi
    fields = '__all__'