from .models import Siswa, Instansi
from .serializers import SiswaSerializer, InstansiSerializer
from rest_framework import viewsets

class SiswaViewset(viewsets.ModelViewSet):
  queryset = Siswa.objects.all().order_by('NIS', 'kelas')
  serializer_class = SiswaSerializer
  http_method_names = ['get']


class InstansiViewset(viewsets.ModelViewSet):
  queryset = Instansi.objects.all().order_by('nama')
  serializer_class = InstansiSerializer
  http_method_names = ['get']