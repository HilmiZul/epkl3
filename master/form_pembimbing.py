from django.forms import ModelForm
from django import forms
from .models import Pembimbing, PembimbingSiswa

class FormPembimbing(ModelForm):
  class Meta:
    model = Pembimbing
    fields = ['nama', 'jurusan']

    labels = {
      'nama': 'Nama',
      'jurusan': 'Jurusan',
    }

    widgets = {
      'nama': forms.TextInput(attrs={
        'id': 'nama',
        'class':'validate form-control',
        'required':'required',
      }),
      'jurusan': forms.Select(attrs={
        'id': 'jurusan',
        'class': 'validate this-select form-control',
        'required': 'required',
      }),
    }

class FormPembimbingSiswa(ModelForm):
  class Meta:
    model = PembimbingSiswa
    fields = ['pembimbing_satu', 'instansi']

    labels = {
      'pembimbing_satu': 'Pembimbing',
      'instansi': 'Instansi',
    }

    widgets = {
      'pembimbing_satu': forms.Select(attrs={
        'id': 'pembimbing_satu',
        'class':'validate this-select',
        'required':'required',
      }),
      'instansi': forms.Select(attrs={
        'id': 'instansi',
        'class': 'validate this-select',
        'required': 'required',
      }),
    }
