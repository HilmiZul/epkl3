from django.urls import path
from .views_surat_create import *
from .views_surat_read import *
from .views_cetak import *
from .views_surat_delete import *
from .views_surat_update import *
from .views_export import *

urlpatterns = [
  path('', get_surat_permohonan, name="get_surat_permohonan"),
  path('tambah/', tambah_surat_permohonan, name="tambah_surat_permohonan"),
  path('hapus/<int:id_surat>', hapus_surat_permohonan, name="hapus_surat_permohonan"),

  path('export/xls/', export_pkl_xls, name='export_pkl_xls'),

  path('rpl/tambah/', tambah_surat_rpl, name='tambah_surat_rpl'),
  path('rpl/', surat_rpl, name='surat_rpl'),
  path('rpl/cetak/<int:id_instansi>', cetak_surat_rpl),
  # path('rpl/hapus/<int:id_surat>', hapus_surat_rpl),
  # path('rpl/ubah/<int:id_surat>', ubah_surat_rpl),
  path('rpl/cetak/ready', cetak_pkl_rpl, name='cetak_pkl_rpl'),
  path('rpl/export/xls', export_instansi_rpl, name='export_instansi_siswa_rpl'),
  path('rpl/cetak/pengantar/<int:id_instansi>', cetak_surat_pengantar_rpl, name='cetak_surat_pengantar_rpl'),

  path('tkj/cetak/<int:id_instansi>', cetak_surat_tkj),
  path('tkj/', surat_tkj, name='surat_tkj'),
  path('tkj/tambah/', tambah_surat_tkj, name='tambah_surat_tkj'),
  path('tkj/hapus/<int:id_surat>', hapus_surat_tkj),
  # path('tkj/ubah/<int:id_surat>', ubah_surat_tkj),
  path('tkj/cetak/ready', cetak_pkl_tkj),
  path('tkj/export/xls', export_instansi_tkj, name='export_instansi_siswa_tkj'),
  path('tkj/cetak/pengantar/<int:id_instansi>', cetak_surat_pengantar_tkj, name='cetak_surat_pengantar_tkj'),
]