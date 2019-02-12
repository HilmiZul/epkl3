from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Permohonan
from master.models import Siswa, Instansi

@login_required(login_url=settings.LOGIN_URL)
def ubah_surat_rpl(request, id_surat):
  if request.POST:
    siswa = Siswa.objects.get(id=request.POST['nama_siswa'])
    instansi = Instansi.objects.get(id=request.POST['nama_instansi'])

    Permohonan.objects.filter(id=id_surat).update(
      nama_siswa = siswa,
      nama_instansi = instansi,
    )
    msg = "Data berhasil diperbaharui."

    surat = Permohonan.objects.get(id=id_surat)
    students_rpl_1 = Siswa.objects.filter(kelas='XII.RPL-1').order_by('kelas')
    students_rpl_2 = Siswa.objects.filter(kelas='XII.RPL-2').order_by('kelas')
    students_rpl_3 = Siswa.objects.filter(kelas='XII.RPL-3').order_by('kelas')
    instansi = Instansi.objects.filter(grup='RPL').order_by('nama')
    return render(request, 'ubah-surat-rpl.html', 
      {
        'msg':msg,
        'surat':surat,
        'students_rpl_1':students_rpl_1,
        'students_rpl_2':students_rpl_2,
        'students_rpl_3':students_rpl_3,
        'instansi':instansi,
      }
    )
  else:
    surat = Permohonan.objects.get(id=id_surat)
    students_rpl_1 = Siswa.objects.filter(kelas='XII.RPL-1').order_by('kelas')
    students_rpl_2 = Siswa.objects.filter(kelas='XII.RPL-2').order_by('kelas')
    students_rpl_3 = Siswa.objects.filter(kelas='XII.RPL-3').order_by('kelas')
    instansi = Instansi.objects.filter(grup='RPL').order_by('nama')
  return render(request, 'ubah-surat-rpl.html', 
    {
      'surat':surat,
      'students_rpl_1':students_rpl_1,
      'students_rpl_2':students_rpl_2,
      'students_rpl_3':students_rpl_3,
      'instansi':instansi,
    }
  )


@login_required(login_url=settings.LOGIN_URL)
def ubah_surat_tkj(request, id_surat):
  if request.POST:
    siswa = Siswa.objects.get(id=request.POST['nama_siswa'])
    instansi = Instansi.objects.get(id=request.POST['nama_instansi'])

    Permohonan.objects.filter(id=id_surat).update(
      nama_siswa = siswa,
      nama_instansi = instansi,
    )
    msg = "Data berhasil diperbaharui."

    surat = Permohonan.objects.get(id=id_surat)
    students_tkj_1 = Siswa.objects.filter(kelas='XII.TKJ-1').order_by('kelas')
    students_tkj_2 = Siswa.objects.filter(kelas='XII.TKJ-2').order_by('kelas')
    students_tkj_3 = Siswa.objects.filter(kelas='XII.TKJ-3').order_by('kelas')
    students_tkj_4 = Siswa.objects.filter(kelas='XII.TKJ-4').order_by('kelas')
    instansi = Instansi.objects.filter(grup='TKJ').order_by('nama')
    return render(request, 'ubah-surat-tkj.html', 
      {
        'msg':msg,
        'surat':surat,
        'students_tkj_1':students_tkj_1,
        'students_tkj_2':students_tkj_2,
        'students_tkj_3':students_tkj_3,
        'students_tkj_4':students_tkj_4,
        'instansi':instansi,
      }
    )
  else:
    surat = Permohonan.objects.get(id=id_surat)
    students_tkj_1 = Siswa.objects.filter(kelas='XII.TKJ-1').order_by('kelas')
    students_tkj_2 = Siswa.objects.filter(kelas='XII.TKJ-2').order_by('kelas')
    students_tkj_3 = Siswa.objects.filter(kelas='XII.TKJ-3').order_by('kelas')
    students_tkj_4 = Siswa.objects.filter(kelas='XII.TKJ-4').order_by('kelas')
    instansi = Instansi.objects.filter(grup='TKJ').order_by('nama')
  return render(request, 'ubah-surat-tkj.html', 
    {
      'surat':surat,
      'students_tkj_1':students_tkj_1,
      'students_tkj_2':students_tkj_2,
      'students_tkj_3':students_tkj_3,
      'students_tkj_4':students_tkj_4,
      'instansi':instansi,
    }
  )