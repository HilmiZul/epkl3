from django.db import models
from django.contrib.auth.models import User
from master.models import Siswa, Pembimbing

# AKUN.PEMBIMBING
class AkunPembimbing(models.Model):
    level_choices = (
        ("root", "root"),
        ("admin", "admin"),
        ("pembimbing", "pembimbing"),
        ("siswa", "siswa"),
    )

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    profil = models.ForeignKey(Pembimbing, null=True, on_delete=models.CASCADE)
    level = models.CharField(max_length=10, choices=level_choices)

    def __str__(self):
        return self.profil.nama


# AKUN.SISWA
class AkunSiswa(models.Model):
  username = models.ForeignKey(User, on_delete=models.CASCADE)
  profil = models.ForeignKey(Siswa, null=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.profil.nama