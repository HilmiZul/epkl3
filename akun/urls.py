from django.urls import path
from .views import masuk, keluar
from .views_siswa import *

urlpatterns = [
  path('masuk/', masuk),
  path('keluar/', keluar),
  
  # akun siswa
  path('login/', masuk_siswa),
  path('logout/', keluar_siswa),
]