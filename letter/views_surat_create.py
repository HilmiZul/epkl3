from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Permohonan
from master.models import Siswa, Instansi

@login_required(login_url=settings.LOGIN_URL)
def tambah_surat_rpl(request):
  if request.POST:
    siswa = Siswa.objects.get(id=request.POST['nama_siswa'])
    instansi = Instansi.objects.get(id=request.POST['nama_instansi'])
    Permohonan(
      nama_siswa = siswa,
      nama_instansi = instansi,
    ).save()   
    Siswa.objects.filter(id=siswa.id).update(pkl=True) 
    msg = "Data berhasil ditambahkan."
    students_rpl_1 = Siswa.objects.filter(kelas='XII.RPL-1', pkl=False).order_by('kelas')
    students_rpl_2 = Siswa.objects.filter(kelas='XII.RPL-2', pkl=False).order_by('kelas')
    students_rpl_3 = Siswa.objects.filter(kelas='XII.RPL-3', pkl=False).order_by('kelas')
    instansi = Instansi.objects.filter(grup='RPL').order_by('nama')
    return render(request, 'tambah-surat-rpl.html', 
      {
        'msg':msg,
        'students_rpl_1':students_rpl_1,
        'students_rpl_2':students_rpl_2,
        'students_rpl_3':students_rpl_3,
        'instansi':instansi,
      }
    )
  else:
    students_rpl_1 = Siswa.objects.filter(kelas='XII.RPL-1', pkl=False).order_by('kelas')
    students_rpl_2 = Siswa.objects.filter(kelas='XII.RPL-2', pkl=False).order_by('kelas')
    students_rpl_3 = Siswa.objects.filter(kelas='XII.RPL-3', pkl=False).order_by('kelas')
    instansi = Instansi.objects.filter(grup='RPL').order_by('nama')
  return render(request, 'tambah-surat-rpl.html', 
    {
      'students_rpl_1':students_rpl_1,
      'students_rpl_2':students_rpl_2,
      'students_rpl_3':students_rpl_3,
      'instansi':instansi,
    }
  )


@login_required(login_url=settings.LOGIN_URL)
def tambah_surat_tkj(request):
  if request.POST:
    siswa = Siswa.objects.get(id=request.POST['nama_siswa'])
    instansi = Instansi.objects.get(id=request.POST['nama_instansi'])
    Permohonan(
      nama_siswa = siswa,
      nama_instansi = instansi,
    ).save()    
    Siswa.objects.filter(id=siswa.id).update(pkl=True)
    msg = "Data berhasil ditambahkan."
    students_tkj_1 = Siswa.objects.filter(kelas='XII.TKJ-1', pkl=False).order_by('kelas')
    students_tkj_2 = Siswa.objects.filter(kelas='XII.TKJ-2', pkl=False).order_by('kelas')
    students_tkj_3 = Siswa.objects.filter(kelas='XII.TKJ-3', pkl=False).order_by('kelas')
    students_tkj_4 = Siswa.objects.filter(kelas='XII.TKJ-4', pkl=False).order_by('kelas')
    instansi = Instansi.objects.filter(grup='TKJ').order_by('nama')
    return render(request, 'tambah-surat-tkj.html', 
      {
        'msg':msg,
        'students_tkj_1':students_tkj_1,
        'students_tkj_2':students_tkj_2,
        'students_tkj_3':students_tkj_3,
        'students_tkj_4':students_tkj_4,
        'instansi':instansi,
      }
    )
  else:
    students_tkj_1 = Siswa.objects.filter(kelas='XII.TKJ-1', pkl=False).order_by('kelas')
    students_tkj_2 = Siswa.objects.filter(kelas='XII.TKJ-2', pkl=False).order_by('kelas')
    students_tkj_3 = Siswa.objects.filter(kelas='XII.TKJ-3', pkl=False).order_by('kelas')
    students_tkj_4 = Siswa.objects.filter(kelas='XII.TKJ-4', pkl=False).order_by('kelas')
    instansi = Instansi.objects.filter(grup='TKJ').order_by('nama')
  return render(request, 'tambah-surat-tkj.html', 
    {
      'students_tkj_1':students_tkj_1,
      'students_tkj_2':students_tkj_2,
      'students_tkj_3':students_tkj_3,
      'students_tkj_4':students_tkj_4,
      'instansi':instansi,
    }
  )