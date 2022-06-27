from statistics import mode
from turtle import ondrag
from django.db import models

# Create your models here.
class Siswa(models.Model):
    kelas_choices = (
        ('RPL', (
            ('XII.RPL-1', 'XII.RPL-1'),
            ('XII.RPL-2', 'XII.RPL-2'),
            ('XII.RPL-3', 'XII.RPL-3'),
            # ('XII.RPL-4', 'XII.RPL-4'),
        )),
        ('TKJ', (
            ('XII.TKJ-1', 'XII.TKJ-1'),
            ('XII.TKJ-2', 'XII.TKJ-2'),
            ('XII.TKJ-3', 'XII.TKJ-3'),
            ('XII.TKJ-4', 'XII.TKJ-4'),
        )),
    )

    program_choices = (
        ('Rekayasa Perangkat Lunak', 'Rekayasa Perangkat Lunak'),
        ('Teknik Komputer dan Jaringan', 'Teknik Komputer dan Jaringan'),
    )
    jk_choices = (
      ('L', 'L'),
      ('P', 'P'),
    )
    NIS = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    jk = models.CharField(max_length=1, choices=jk_choices, null=True)
    kelas = models.CharField(max_length=15, choices=kelas_choices)
    program_ahli = models.CharField(max_length=30, choices=program_choices)
    pkl = models.BooleanField(default=False)
    status_judul = models.BooleanField(default=False)
    pembimbing = models.BooleanField(default=False)
    isRapotTuntas = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.nama

class Instansi(models.Model):
    program_keahlian_choices = (
        ('RPL', 'RPL'),
        ('TKJ', 'TKJ'),
    )
    gender_choices = (
      ('Semua', 'Semua'),
      ('L', 'L'),
      ('P', 'P'),
    )
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    pimpinan = models.CharField(max_length=50, null=True, blank=True)
    pembimbing = models.CharField(max_length=50, null=True)
    kontak = models.CharField(max_length=13, null=True)
    email = models.EmailField(max_length=80, null=True)
    program_keahlian = models.CharField(max_length=3, choices=program_keahlian_choices, default=True, blank=True)
    kuota = models.IntegerField(null=True)
    slot = models.IntegerField(null=True, blank=True, default=0)
    gender = models.CharField(max_length=5, choices=gender_choices, null=True, blank=True)

    def __str__(self):
        return self.nama

# class InstansiTKJ(models.Model):
#     nama = models.CharField(max_length=100)
#     alamat = models.TextField()

#     def __str__(self):
#         return self.nama

class Pembimbing(models.Model):
    jurusan_choices = (
        ('RPL', 'RPL'),
        # ('TKJ', 'TKJ'),
    )

    nama = models.CharField(max_length=40)
    jurusan = models.CharField(max_length=3, choices=jurusan_choices)

    def __str__(self):
        return self.nama


class PembimbingSiswa(models.Model):
    pembimbing_satu = models.ForeignKey(Pembimbing, related_name="pembimbing_satu", null=True, on_delete=models.CASCADE)
    # pembimbing_dua = models.ForeignKey(Pembimbing, related_name="pembimbing_dua", null=True, on_delete=models.CASCADE)
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    # instansi = models.ForeignKey(Instansi, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pembimbing_satu.nama


class KompetensiDasar(models.Model):
    jurusan_choices = (
        ('TKJ', 'TKJ'),
        ('RPL', 'RPL'),
    )
    kode        = models.CharField(max_length=4)
    nama        = models.CharField(max_length=70)
    jurusan     = models.CharField(max_length=3, choices=jurusan_choices)

    def __str__(self):
        return self.kode
