from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Instansi

@login_required(login_url=settings.LOGIN_URL)
def instansi_rpl(request):
  instansi = Instansi.objects.filter(program_keahlian='RPL').order_by('nama')
  return render(request, 'instansi-rpl.html', {'instansi': instansi})

@login_required(login_url=settings.LOGIN_URL)
def instansi_tkj(request):
  instansi = Instansi.objects.filter(program_keahlian='TKJ').order_by('nama')
  return render(request, 'instansi-tkj.html', {'instansi': instansi})