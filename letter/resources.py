from .models import Permohonan
from import_export import resources

class PermohonanResource(resources.ModelResource):
  class Meta:
    model = Permohonan
    fields = [
      'nama_instansi__nama',
      'nama_instansi__alamat',
      'nama_siswa__nama',
      'nama_siswa__kelas',
    ]