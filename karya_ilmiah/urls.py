from django.urls import path
from .views import *
from .views_admin import *

urlpatterns = [
  # area.siswa
  path('judul/submit/', submit_judul),
  path('judul/', show_judul),
  path('judul/ubah/<int:id>', ubah_judul),

  # area.admin.dan.mentor
  path('rpl/pengajuan-judul/', pengajuan_judul),
  path('rpl/pengajuan-judul/setuju/<int:id>', setuju_submission_judul),
  path('rpl/pengajuan-judul/tolak/<int:id>', dikembalikan_submission_judul),
]