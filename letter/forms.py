from django.forms import ModelForm
from django import forms
from .models import Permohonan

class FormPermohonan(ModelForm):
  class Meta:
    model = Permohonan
    fields = '__all__'

    widgets = {
      'nama_siswa' : forms.Select(attrs={
        'id': 'nama_siswa',
        'class': 'validate this-select form-control',
        'required': 'required',
      }),
      'nama_instansi' : forms.Select(attrs={
        'id': 'nama_instansi',
        'class': 'validate this-select form-control',
        'required': 'required',
      }),
    }