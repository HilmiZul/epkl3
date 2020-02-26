from django.db import models
from akun.models import AkunSiswa
from master.models import PembimbingSiswa, KompetensiDasar

class Jurnal(models.Model):
  siswa       = models.ForeignKey(AkunSiswa, on_delete=models.CASCADE)
  pembimbing  = models.ForeignKey(PembimbingSiswa, on_delete=models.CASCADE)
  tanggal     = models.DateTimeField(auto_now=True)
  kegiatan    = models.TextField()
  foto        = models.ImageField(upload_to='foto')
  verify      = models.BooleanField(default=False)
  status      = models.BooleanField(default=True)
  kd          = models.ForeignKey(KompetensiDasar, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.siswa.profil.nama
  
