from django.urls import path
from .views_master import *
from .views_pembimbing import *
from .views_export_instansi import *

urlpatterns = [
  path('', get_master_peserta, name="get_master_peserta"),
  path('peserta/', get_master_peserta, name="get_master_peserta"),

  path('instansi/', get_master_instansi, name='get_master_instansi'),
  path('instansi/tambah/', master_tambah_instansi, name='tambah_instansi'),
  path('instansi/ubah/<int:id_instansi>', master_ubah_instansi, name='master_ubah_instansi'),
  path('instansi/hapus/<int:id_instansi>', master_hapus_instansi, name='master_hapus_instansi'),
  
  path('pembimbing/', pembimbing, name='get_master_pembimbing'),
  path('pembimbing/tambah/', tambah_pembimbing, name='tambah_pembimbing'),
  path('pembimbing/ubah/<int:id>', ubah_pembimbing, name='ubah_pembimbing'),
  path('pembimbing/hapus/<int:id>', hapus_pembimbing, name='hapus_pembimbing'),

  path('export/xls/', export_instansi, name='ex_instansi'),
]