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
        'class':'validate',
        'required':'required',
      }),
      'jurusan': forms.Select(attrs={
        'id': 'jurusan',
        'class': 'validate this-select',
        'required': 'required',
      }),
    }

class FormPembimbingSiswa(ModelForm):
  class Meta:
    model = PembimbingSiswa
    fields = ['pembimbing_satu', 'pembimbing_dua', 'siswa']

    labels = {
      'pembimbing_satu': 'Pembimbing Satu',
      'pembimbing_dua': 'Pembimbing Dua',
      'siswa': 'Siswa',
    }

    widgets = {
      'pembimbing_satu': forms.Select(attrs={
        'id': 'pembimbing_satu',
        'class':'validate this-select',
        'required':'required',
      }),
      'pembimbing_dua': forms.Select(attrs={
        'id': 'pembimbing_dua',
        'class':'validate this-select',
        'required':'required',
      }),
      'siswa': forms.Select(attrs={
        'id': 'siswa',
        'class': 'validate this-select',
        'required': 'required',
      }),
    }
