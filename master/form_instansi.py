from django.forms import ModelForm
from django import forms
from .models import Instansi

class FormTambahInstansi(ModelForm):
  class Meta:
    model = Instansi
    exclude = ['slot', 'program_keahlian']

    widgets = {
      'nama': forms.TextInput(attrs={
        'id': 'nama',
        'class':'validate form-control',
        'required':'required',
      }),
      'alamat': forms.Textarea(attrs={
        'id': 'alamat',
        'class':'validate form-control',
        'required':'required',
        'rows': 4
      }),
      'pimpinan': forms.TextInput(attrs={
        'id': 'pimpinan',
        'class':'validate form-control',
        'required':'required',
      }),
      'pembimbing': forms.TextInput(attrs={
        'id': 'pembimbing',
        'class':'validate form-control',
        'required':'required',
      }),
      'kontak': forms.TextInput(attrs={
        'id': 'kontak',
        'class':'validate form-control',
        'required':'required',
        'type': 'number'
      }),
      'email': forms.TextInput(attrs={
        'id': 'email',
        'class':'validate form-control',
        'required':'required',
        'type': 'email',
      }),
      'program_keahlian': forms.Select(attrs={
        'id': 'program_keahlian',
        'class': 'validate this-select form-control',
        'required': 'required',
      }),
      'kuota': forms.TextInput(attrs={
        'id': 'kuota',
        'class':'validate form-control',
        'required':'required',
        'type': 'number',
      }),
      'gender': forms.Select(attrs={
        'id': 'gender',
        'class': 'validate this-select form-control',
        'required': 'required',
      }),
    }
