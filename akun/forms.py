from django.forms import ModelForm
from .models import AkunSiswa
from django import forms

class FormTambahAkunSiswa(ModelForm):
  class Meta:
    model = AkunSiswa
    fields = '__all__'

    widgets = {
      'username': forms.Select(attrs={
        'class':'form-control select-username mb-3',
        'required':'required',
      }),
      'profil': forms.Select(attrs={
        'class':'form-control select-profile',
        'required':'required',
      }),
    }