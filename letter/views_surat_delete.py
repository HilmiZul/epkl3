from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Permohonan
from master.models import Siswa, Instansi

@login_required(login_url=settings.LOGIN_URL)
def hapus_surat_rpl(request, id_surat):
  # ambil status pkl dari Siswa sebelum dihapus
  # dan ubah status pkl menjadi false
  surat = Permohonan.objects.get(id=id_surat)
  get_instansi = Instansi.objects.get(id=surat.nama_instansi.id)
  Siswa.objects.filter(id=surat.nama_siswa.id).update(pkl=False)

  # hapus
  Permohonan.objects.filter(id=id_surat).delete()

  # limit instansi -1
  cur_limit = get_instansi.limit - 1
  Instansi.objects.filter(id=get_instansi.id).update(limit=cur_limit)

  get_surat = Permohonan.objects.filter(nama_siswa__program_ahli='Rekayasa Perangkat Lunak').order_by('nama_instansi')
  msg = 'Data berhasil dihapus.'
  return render(request, 'surat-rpl.html', 
    {
      'msg':msg, 
      'surat':get_surat
    }
  )


@login_required(login_url=settings.LOGIN_URL)
def hapus_surat_tkj(request, id_surat):
  # ambil status pkl dari Siswa sebelum dihapus
  # dan ubah status pkl menjadi false...
  surat = Permohonan.objects.get(id=id_surat)
  get_instansi = Instansi.objects.get(id=surat.nama_instansi.id)
  Siswa.objects.filter(id=surat.nama_siswa.id).update(pkl=False)

  # hapus
  Permohonan.objects.filter(id=id_surat).delete()

  # limit instansi -1
  cur_limit = get_instansi.limit - 1
  Instansi.objects.filter(id=get_instansi.id).update(limit=cur_limit)
  
  get_surat = Permohonan.objects.filter(nama_siswa__program_ahli='Teknik Komputer dan Jaringan').order_by('nama_instansi')
  msg = 'Data berhasil dihapus.'
  return render(request, 'surat-tkj.html', 
    {
      'msg':msg, 
      'surat':get_surat
    }
  )