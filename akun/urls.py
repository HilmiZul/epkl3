from django.urls import path
from .views import masuk, keluar

urlpatterns = [
  path('masuk/', masuk),
  path('keluar/', keluar),
]