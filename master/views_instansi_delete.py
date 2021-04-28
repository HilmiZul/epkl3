from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Instansi
from django.contrib import messages

@login_required(login_url=settings.LOGIN_URL)
def hapus_instansi_rpl(request, id_instansi):
  Instansi.objects.filter(id=id_instansi).delete()
  msg = "Data berhasil dihapus."
  messages.success(request, msg)
  return redirect('instansi_rpl')
  


@login_required(login_url=settings.LOGIN_URL)
def hapus_instansi_tkj(request, id_instansi):
  Instansi.objects.filter(id=id_instansi).delete()
  msg = "Data berhasil dihapus."
  messages.success(request, msg)
  return redirect('instansi_tkj')
  
