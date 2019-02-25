from django.urls import path
from .views import *
from .views_admin import *

urlpatterns = [
  # area.siswa
  path('judul/submit/', submit_judul),
  path('judul/', show_judul),
  path('judul/ubah/<int:id>', ubah_judul),

  # area.mentor
  path('pengajuan-judul/', pengajuan_judul),
  path('pengajuan-judul/setuju/<int:id>', setuju_submission_judul),
  path('pengajuan-judul/tolak/<int:id>', dikembalikan_submission_judul),

  # area.admin
  path('pengajuan-judul/', pengajuan_judul_admin),
]