from django.forms import ModelForm
from django import forms
from .models import Pembimbing, PembimbingSiswa

class FormPembimbing(ModelForm):
  class Meta:
    model = Pembimbing
    fields = ['nama', 'program_keahlian']

    labels = {
      'nama': 'Nama',
      'program_keahlian': 'Program Keahlian',
    }

    widgets = {
      'nama': forms.TextInput(attrs={
        'id': 'nama',
        'class':'validate form-control',
        'required':'required',
      }),
      'program_keahlian': forms.Select(attrs={
        'id': 'program_keahlian',
        'class': 'validate this-select form-control',
        'required': 'required',
      }),
    }

class FormPembimbingSiswa(ModelForm):
  class Meta:
    model = PembimbingSiswa
    fields = ['pembimbing_satu', 'siswa']

    labels = {
      'pembimbing_satu': 'Pembimbing',
      'siswa': 'Siswa',
    }

    widgets = {
      'pembimbing_satu': forms.Select(attrs={
        'id': 'pembimbing_satu',
        'class':'validate this-select',
        'required':'required',
      }),
      'siswa': forms.Select(attrs={
        'id': 'siswa',
        'class': 'validate this-select',
        'required': 'required',
      }),
    }
