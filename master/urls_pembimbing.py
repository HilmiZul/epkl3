from django.urls import path
from .views_pembimbing import *

urlpatterns = [
  path('', pembimbing),
  path('tambah/', tambah_pembimbing),
  path('ubah/<int:id>', ubah_pembimbing),
  path('hapus/<int:id>', hapus_pembimbing),
  
  path('siswa/', pembimbing_siswa),
  path('siswa/tambah/', tambah_pembimbing_siswa),
  # path('siswa/ubah/<int:id>', ubah_pembimbing_siswa),
  path('siswa/hapus/<int:id>', hapus_pembimbing_siswa),
]