from django.urls import path
from .views import masuk, keluar
from .views_siswa import *
from dashboard.views import dashboard_siswa

urlpatterns = [
  path('home/', dashboard_siswa),
  
  path('', masuk),
  path('masuk/', masuk),
  path('keluar/', keluar),
  
  # akun siswa
  path('login/', masuk_siswa),
  path('logout/', keluar_siswa),
]