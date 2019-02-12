from django.urls import path
from .views_surat_create import *
from .views_surat_read import *
from .views_cetak import *
from .views_surat_delete import *
from .views_surat_update import *

urlpatterns = [
  path('rpl/tambah/', tambah_surat_rpl),
  path('rpl/', surat_rpl),
  path('rpl/cetak/<int:id_instansi>', cetak_surat_rpl),
  path('rpl/hapus/<int:id_surat>', hapus_surat_rpl),
  path('rpl/ubah/<int:id_surat>', ubah_surat_rpl),

  path('tkj/cetak/<int:id_instansi>', cetak_surat_tkj),
  path('tkj/', surat_tkj),
  path('tkj/tambah/', tambah_surat_tkj),
  path('tkj/hapus/<int:id_surat>', hapus_surat_tkj),
  path('tkj/ubah/<int:id_surat>', ubah_surat_tkj),
]