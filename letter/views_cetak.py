from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Permohonan
from master.models import Instansi

@login_required(login_url=settings.LOGIN_URL)
def cetak_surat_rpl(request, id_instansi):
  surat = Permohonan.objects.filter(nama_instansi__id=id_instansi)
  instansi = Instansi.objects.get(id=id_instansi)
  return render(request, 'cetak.html', {'surat':surat, 'instansi':instansi})


@login_required(login_url=settings.LOGIN_URL)
def cetak_surat_tkj(request, id_instansi):
  surat = Permohonan.objects.filter(nama_instansi__id=id_instansi)
  instansi = Instansi.objects.get(id=id_instansi)
  return render(request, 'cetak.html', {'surat':surat, 'instansi':instansi})