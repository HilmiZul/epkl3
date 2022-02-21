from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Permohonan
from master.models import Instansi
from datetime import datetime

@login_required(login_url=settings.LOGIN_URL)
def cetak_surat_rpl(request, id_instansi):
  surat = Permohonan.objects.filter(nama_instansi__id=id_instansi)
  instansi = Instansi.objects.get(id=id_instansi)
  # tanggal sekarang
  tanggal = datetime.now()
  tanggal = tanggal.strftime("%d %B %Y")
  return render(request, 'cetak.html', 
    {
      'surat':surat, 
      'instansi':instansi,
      'tanggal': tanggal,
    }
  )


@login_required(login_url=settings.LOGIN_URL)
def cetak_surat_tkj(request, id_instansi):
  surat = Permohonan.objects.filter(nama_instansi__id=id_instansi)
  instansi = Instansi.objects.get(id=id_instansi)
  # tanggal sekarang
  tanggal = datetime.now()
  tanggal = tanggal.strftime("%d %B %Y")
  return render(request, 'cetak.html', 
    {
      'surat':surat, 
      'instansi':instansi,
      'tanggal': tanggal,
    }
  )


# REPORT.
# YANG SUDAH MENDAPATKAN TEMPAT PKL
@login_required(login_url=settings.LOGIN_URL)
def cetak_pkl_rpl(request):
    fix = Permohonan.objects.filter(nama_siswa__pkl=True, nama_siswa__program_ahli='Rekayasa Perangkat Lunak').order_by('nama_siswa__kelas')
    program_ahli = "Rekayasa Perangkat Lunak"
    # tanggal sekarang
    tanggal = datetime.now()
    tanggal = tanggal.strftime("%d %B %Y")
    return render(request, 'cetak-siswa-pkl-rpl.html', 
      {
        'surat':fix,
        'program_ahli':program_ahli,
        'tanggal':tanggal
      }
    )

@login_required(login_url=settings.LOGIN_URL)
def cetak_pkl_tkj(request):
    fix = Permohonan.objects.filter(nama_siswa__pkl=True, nama_siswa__program_ahli='Teknik Komputer dan Jaringan').order_by('nama_siswa__kelas')
    program_ahli = "Teknik Komputer dan Jaringan"
    # tanggal sekarang
    tanggal = datetime.now()
    tanggal = tanggal.strftime("%d %B %Y")
    return render(request, 'cetak-siswa-pkl-tkj.html', 
      {
        'surat':fix,
        'program_ahli':program_ahli,
        'tanggal':tanggal
      }
    )

@login_required(login_url=settings.LOGIN_URL)
def cetak_rpl_belum_pkl(request):
    siswa = Siswa.objects.filter(pkl=False, program_ahli='Rekayasa Perangkat Lunak').order_by('NIS')
    count = siswa.count()
    return render(request, 'cetak-rpl-belum-pkl.html', {'siswa':siswa, 'count':count})


@login_required(login_url=settings.LOGIN_URL)
def cetak_surat_pengantar_rpl(request, id_instansi):
  surat = Permohonan.objects.filter(nama_instansi__id=id_instansi)
  instansi = Instansi.objects.get(id=id_instansi)
  # tanggal sekarang
  tanggal = datetime.now()
  tanggal = tanggal.strftime("%d %B %Y")
  return render(request, 'cetak-memo-kaprog.html', 
    {
      'surat':surat, 
      'instansi':instansi,
      'tanggal': tanggal,
    }
  )

@login_required(login_url=settings.LOGIN_URL)
def cetak_surat_pengantar_tkj(request, id_instansi):
  surat = Permohonan.objects.filter(nama_instansi__id=id_instansi)
  instansi = Instansi.objects.get(id=id_instansi)
  # tanggal sekarang
  tanggal = datetime.now()
  tanggal = tanggal.strftime("%d %B %Y")
  return render(request, 'cetak-pengantar.html', 
    {
      'surat':surat, 
      'instansi':instansi,
      'tanggal': tanggal,
    }
  )
