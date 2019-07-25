from django.db import models
from akun.models import AkunSiswa
from master.models import PembimbingSiswa

# Create your models here.
class SubmissionJudul(models.Model):
  judul = models.TextField()
  tanggal = models.DateTimeField(auto_now_add=True)
  tanggal_acc = models.DateTimeField(null=True)
  submit_status = models.BooleanField() # True=udah kirim. False=belum kirim
  status = models.CharField(max_length=12, null=True) # Kalo udah kirim, statusnya menunggu untuk diriview.
                                                      # setelah diriview, status dikembalikan apabila kurang ilmiah
                                                      # apabila judul sesuai dan ilmiah, status akan "Diterima"
  siswa = models.ForeignKey(AkunSiswa, on_delete=models.CASCADE)
  pembimbing = models.ForeignKey(PembimbingSiswa, on_delete=models.CASCADE)
  catatan = models.TextField(null=True)

  def __str__(self):
    return self.judul


class Bimbingan(models.Model):
  bab_choices = (
    ('BAB I', 'BAB I'),
    ('BAB II', 'BAB II'),
    ('BAB III', 'BAB III'),
    ('BAB IV', 'BAB IV'),
    ('BAB V', 'BAB V'),
  )

  judul = models.ForeignKey(SubmissionJudul, on_delete=models.CASCADE)
  bab = models.CharField(max_length=7, choices=bab_choices)
  tanggal = models.DateField(auto_now_add=True)
  berkas = models.FileField(upload_to='berkas/')
  status = models.BooleanField(default=True)
  siswa = models.ForeignKey(AkunSiswa, default=True, on_delete=models.CASCADE)
  pembimbing = models.ForeignKey(PembimbingSiswa, default=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.bab