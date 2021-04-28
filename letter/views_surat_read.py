from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Permohonan

@login_required(login_url=settings.LOGIN_URL)
def get_surat_permohonan(request):
  surat = Permohonan.objects.all().order_by('nama_instansi')
  return render(request, 'surat-permohonan.html', {'surat':surat})


@login_required(login_url=settings.LOGIN_URL)
def surat_rpl(request):
  surat = Permohonan.objects.filter(nama_siswa__program_ahli='Rekayasa Perangkat Lunak').order_by('nama_instansi')
  return render(request, 'surat-rpl.html', {'surat':surat})


@login_required(login_url=settings.LOGIN_URL)
def surat_tkj(request):
  surat = Permohonan.objects.filter(nama_siswa__program_ahli='Teknik Komputer dan Jaringan').order_by('nama_instansi')
  return render(request, 'surat-tkj.html', {'surat':surat})