from django.db import models

# Create your models here.
class Siswa(models.Model):
    kelas_choices = (
        ('RPL', (
            ('XI.RPL-1', 'XI.RPL-1'),
            ('XI.RPL-2', 'XI.RPL-2'),
            ('XI.RPL-3', 'XI.RPL-3'),
        )),
        ('TKJ', (
            ('XI.TKJ-1', 'XI.TKJ-1'),
            ('XI.TKJ-2', 'XI.TKJ-2'),
            ('XI.TKJ-3', 'XI.TKJ-3'),
            ('XI.TKJ-4', 'XI.TKJ-4'),
        )),
    )

    program_choices = (
        ('Teknik Komputer dan Jaringan', 'Teknik Komputer dan Jaringan'),
        ('Rekayasa Perangkat Lunak', 'Rekayasa Perangkat Lunak'),
    )

    NIS = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    kelas = models.CharField(max_length=15, choices=kelas_choices)
    program_ahli = models.CharField(max_length=30, choices=program_choices)
    pkl = models.BooleanField(default=False)
    status_judul = models.BooleanField(default=False)
    pembimbing = models.BooleanField(default=False)

    def __str__(self):
        return self.nama

class Instansi(models.Model):
    grup_choices = (
        ('TKJ', 'TKJ'),
        ('RPL', 'RPL'),
    )
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    pimpinan = models.CharField(max_length=50, null=True)
    kontak = models.CharField(max_length=13, null=True)
    email = models.EmailField(max_length=80, null=True)
    grup = models.CharField(max_length=3, choices=grup_choices, default=True)
    limit = models.IntegerField(null=True)

    def __str__(self):
        return self.nama

# class InstansiTKJ(models.Model):
#     nama = models.CharField(max_length=100)
#     alamat = models.TextField()

#     def __str__(self):
#         return self.nama

class Pembimbing(models.Model):
    jurusan_choices = (
        ('TKJ', 'TKJ'),
        ('RPL', 'RPL'),
    )

    nama = models.CharField(max_length=40)
    jurusan = models.CharField(max_length=3, choices=jurusan_choices)

    def __str__(self):
        return self.nama


class PembimbingSiswa(models.Model):
    pembimbing_satu = models.ForeignKey(Pembimbing, related_name="pembimbing_satu", null=True, on_delete=models.CASCADE)
    pembimbing_dua = models.ForeignKey(Pembimbing, related_name="pembimbing_dua", null=True, on_delete=models.CASCADE)
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)

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