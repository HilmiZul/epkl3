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
    fields = ['pembimbing', 'siswa']

    labels = {
      'pembimbing': 'Pembimbing',
      'siswa': 'Siswa',
    }

    widgets = {
      'pembimbing': forms.Select(attrs={
        'id': 'pembimbing',
        'class':'validate this-select',
        'required':'required',
      }),
      'siswa': forms.Select(attrs={
        'id': 'siswa',
        'class': 'validate this-select',
        'required': 'required',
      }),
    }
