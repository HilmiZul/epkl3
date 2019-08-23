from django.urls import path
from .views import *
from .views_admin import *

urlpatterns = [
  # area.siswa
  path('judul/submit/', submit_judul, name='submit_judul'),
  path('timeline/', show_timeline, name='timeline'),
  path('judul/ubah/<int:id>', ubah_judul, name='ubah_judul'),
  path('bimbingan/submit/', bimbingan_submit, name='bimbingan_submit'),
  path('bimbingan/revisi/<int:id>', bimbingan_submit_revisi, name='bimbingan_submit_revisi'),
  path('bimbingan/setujui/<int:id>', setujui_bimbingan_isi, name='setujui_bimbingan_isi'),

  # area.mentor
  path('pengajuan-judul/', pengajuan_judul),
  path('pengajuan-judul/setuju/<int:id>', setuju_submission_judul),
  path('pengajuan-judul/tolak/<int:id>', dikembalikan_submission_judul),

  # area.admin
  # path('pengajuan-judul/', pengajuan_judul_admin),
  path('bimbingan-isi/', bimbingan_isi, name='bimbingan_isi'),
  path('bimbingan-isi/revisi/<int:id>', bimbingan_isi_revisi, name='bimbingan_isi_revisi'),
]