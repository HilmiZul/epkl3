from .models import Siswa, Instansi
from .serializers import SiswaSerializer, InstansiSerializer
from rest_framework import viewsets

class SiswaViewset(viewsets.ModelViewSet):
  queryset = Siswa.objects.filter(isRapotTuntas=True, pkl=False)
  serializer_class = SiswaSerializer


class InstansiViewset(viewsets.ModelViewSet):
  queryset = Instansi.objects.all().order_by('nama')
  serializer_class = InstansiSerializer