from django.forms import ModelForm
from django import forms
from .models import Bimbingan

class FormBimbingan(ModelForm):
  class Meta:
    model = Bimbingan
    exclude = ('status',)
    
    widgets = {
      'bab': forms.Select(attrs={'class':'form-control'}),
      'berkas': forms.TextInput(attrs={'type':'file', 'accept':'.doc, .docx', 'class':'form-control'}),
    }