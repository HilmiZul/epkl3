from django.urls import path
from .views_instansi_create import *
from .views_instansi_read import *
from .views_instansi_update import *
from .views_instansi_delete import *

urlpatterns = [
  path('tambah/', tambah_instansi),

  path('rpl/tambah/', tambah_instansi_rpl),
  path('rpl/', instansi_rpl),
  path('rpl/ubah/<int:id_instansi>', ubah_instansi_rpl),
  path('rpl/hapus/<int:id_instansi>', hapus_instansi_rpl),

  path('tkj/tambah/', tambah_instansi_tkj),
  path('tkj/', instansi_tkj),
  path('tkj/ubah/<int:id_instansi>', ubah_instansi_tkj),
  path('tkj/hapus/<int:id_instansi>', hapus_instansi_tkj),

]