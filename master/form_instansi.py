from django.forms import ModelForm
from .models import Instansi

class FormTambahInstansi(ModelForm):
  class Meta:
    model = Instansi
    fields = '__all__'
