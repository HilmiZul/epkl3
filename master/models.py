from django.db import models

# Create your models here.
class Siswa(models.Model):
    kelas_choices = (
        ('XII.RPL-1', 'XII.RPL-1'),
        ('XII.RPL-2', 'XII.RPL-2'),
        ('XII.RPL-3', 'XII.RPL-3'),
        ('XII.TKJ-1', 'XII.TKJ-1'),
        ('XII.TKJ-2', 'XII.TKJ-2'),
        ('XII.TKJ-3', 'XII.TKJ-3'),
        ('XII.TKJ-4', 'XII.TKJ-4'),
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

    def __str__(self):
        return self.nama

class Instansi(models.Model):
    grup_choices = (
        ('TKJ', 'TKJ'),
        ('RPL', 'RPL'),
    )
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    grup = models.CharField(max_length=3, choices=grup_choices, default=True)

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
    pembimbing = models.ForeignKey(Pembimbing, on_delete=models.CASCADE)
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)

    def __str__(self):
        return self.pembimbing.nama