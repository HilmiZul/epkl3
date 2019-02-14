from django.urls import path
from .views import *
from .views_admin import *

urlpatterns = [
  path('submission-judul/', submission_judul),
  path('show-submit-judul/', show_submit_judul),
  path('judul/ubah/<int:id>', ubah_judul),

  path('show-submission-judul/', show_submission_judul),
  path('show-submission-judul/setuju/<int:id>', setuju_submission_judul),
  path('show-submission-judul/tolak/<int:id>', dikembalikan_submission_judul),
]