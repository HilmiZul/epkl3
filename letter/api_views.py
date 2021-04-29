from .models import Permohonan, Siswa, Instansi
from .serializers import PermohonanSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class PermohonanViewset(viewsets.ModelViewSet):
  queryset = Permohonan.objects.all()
  serializer_class = PermohonanSerializer
  http_method_names = ['get']

  @action(methods=['post'], detail=True)
  def permohonan(self, request, *args, **kwargs):
    Siswa.objects.filter(id=request.nama_siswa.id).update(pkl=True)
    instansi = Instansi.objects.get(id=request.nama_instansi.id)
    cur_slot = instansi.slot + 1
    Instansi.objects.filter(id=instansi.id).update(slot=cur_slot)
    return Response(status=status.HTTP_204_NO_CONTENT)

  # def post(self, request):
  #   data = request.data
  #   siswa_id = data['nama_siswa']
  #   instansi_id = data['nama_instansi']
  #   print(siswa_id)
    # siswa = Siswa.objects.filter(id=siswa_id)
    # siswa.update(pkl=True)
    # instansi = Instansi.objects.filter(id=instansi_id)
    # cur_slot = instansi.slot + 1
    # Instansi.objects.filter(id=instansi_id).update(slot=cur_slot)
    # return Response(status=status.HTTP_200_OK)
