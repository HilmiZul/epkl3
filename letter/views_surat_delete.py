from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Permohonan
from master.models import Siswa, Instansi
from django.contrib import messages


@login_required(login_url=settings.LOGIN_URL)
def hapus_surat_permohonan(request, id_surat):
  # ambil status pkl dari Siswa sebelum dihapus
  # dan ubah status pkl menjadi false
  surat = Permohonan.objects.get(id=id_surat)
  get_instansi = Instansi.objects.get(id=surat.nama_instansi.id)
  Siswa.objects.filter(id=surat.nama_siswa.id).update(pkl=False)

  # hapus
  Permohonan.objects.filter(id=id_surat).delete()

  # limit slot instansi -1
  cur_slot = get_instansi.slot - 1
  Instansi.objects.filter(id=get_instansi.id).update(slot=cur_slot)

  get_surat = Permohonan.objects.all().order_by('nama_instansi')
  msg = 'Data berhasil dihapus.'
  messages.success(request, msg)
  return redirect('get_surat_permohonan')


@login_required(login_url=settings.LOGIN_URL)
def hapus_surat_tkj(request, id_surat):
  # ambil status pkl dari Siswa sebelum dihapus
  # dan ubah status pkl menjadi false...
  surat = Permohonan.objects.get(id=id_surat)
  get_instansi = Instansi.objects.get(id=surat.nama_instansi.id)
  Siswa.objects.filter(id=surat.nama_siswa.id).update(pkl=False)

  # hapus
  Permohonan.objects.filter(id=id_surat).delete()

  # limit slot instansi -1
  cur_slot = get_instansi.slot - 1
  Instansi.objects.filter(id=get_instansi.id).update(slot=cur_slot)
  
  get_surat = Permohonan.objects.filter(nama_siswa__program_ahli='Teknik Komputer dan Jaringan').order_by('nama_instansi')
  msg = 'Data berhasil dihapus.'
  return render(request, 'surat-tkj.html', 
    {
      'msg':msg, 
      'surat':get_surat
    }
  )