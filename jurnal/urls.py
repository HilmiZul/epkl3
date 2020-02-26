from django.urls import path
from .views import timeline

urlpatterns = [
  path('timeline/', timeline, name='jurnal_timeline'),
]