from django.db import models
from master.models import Siswa, Instansi

# Create your models here.
class Permohonan(models.Model):
    nama_siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    nama_instansi = models.ForeignKey(Instansi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_instansi.nama

# class PermohonanTKJ(models.Model):
#     nama_siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
#     nama_instansi = models.ForeignKey(InstansiTKJ, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nama_instansi.nama
