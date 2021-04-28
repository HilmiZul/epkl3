from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Permohonan
from master.models import Siswa, Instansi
from .forms import FormPermohonan
from django.db.models import Q
from django.contrib import messages



@login_required(login_url=settings.LOGIN_URL)
def tambah_surat_permohonan(request):
  if request.POST:
    siswa = Siswa.objects.get(id=request.POST['nama_siswa'])
    instansi_temp = Instansi.objects.get(id=request.POST['nama_instansi'])
    Permohonan(
      nama_siswa = siswa,
      nama_instansi = instansi_temp,
    ).save()   

    # ubah status pkl siswa menjadi True
    Siswa.objects.filter(id=siswa.id).update(pkl=True) 

    # ubah limit slot instansi +1
    cur_slot = instansi_temp.slot + 1
    Instansi.objects.filter(id=instansi_temp.id).update(slot=cur_slot)

    messages.success(request, "Data berhaisl ditambahkan.")
    students_rpl_1 = Siswa.objects.filter(kelas='XII.RPL-1', pkl=False).order_by('kelas')
    students_rpl_2 = Siswa.objects.filter(kelas='XII.RPL-2', pkl=False).order_by('kelas')
    students_rpl_3 = Siswa.objects.filter(kelas='XII.RPL-3', pkl=False).order_by('kelas')
    students_rpl_4 = Siswa.objects.filter(kelas='XII.RPL-4', pkl=False).order_by('kelas')
    students_tkj_1 = Siswa.objects.filter(kelas='XII.TKJ-1', pkl=False).order_by('kelas')
    students_tkj_2 = Siswa.objects.filter(kelas='XII.TKJ-2', pkl=False).order_by('kelas')
    students_tkj_3 = Siswa.objects.filter(kelas='XII.TKJ-3', pkl=False).order_by('kelas')
    students_tkj_4 = Siswa.objects.filter(kelas='XII.TKJ-4', pkl=False).order_by('kelas')
    instansi_temp = Instansi.objects.all().order_by('nama')
    for ins in instansi_temp:
      # filter instansi, hanya menampilkan yang limit-nya <= kuota
      instansi = Instansi.objects.filter(slot__lt=ins.kuota).order_by('nama')
    return redirect('tambah_surat_permohonan')
    # return render(request, 'tambah-surat-permohonan.html', 
    #   {
    #     'students_rpl_1':students_rpl_1,
    #     'students_rpl_2':students_rpl_2,
    #     'students_rpl_3':students_rpl_3,
    #     'students_rpl_4':students_rpl_4,
    #     'students_tkj_1':students_tkj_1,
    #     'students_tkj_2':students_tkj_2,
    #     'students_tkj_3':students_tkj_3,
    #     'students_tkj_4':students_tkj_4,
    #     'instansi':instansi,
    #   }
    # )
  else:
    students_rpl_1 = Siswa.objects.filter(kelas='XII.RPL-1', pkl=False).order_by('kelas')
    students_rpl_2 = Siswa.objects.filter(kelas='XII.RPL-2', pkl=False).order_by('kelas')
    students_rpl_3 = Siswa.objects.filter(kelas='XII.RPL-3', pkl=False).order_by('kelas')
    students_rpl_4 = Siswa.objects.filter(kelas='XII.RPL-4', pkl=False).order_by('kelas')
    students_tkj_1 = Siswa.objects.filter(kelas='XII.TKJ-1', pkl=False).order_by('kelas')
    students_tkj_2 = Siswa.objects.filter(kelas='XII.TKJ-2', pkl=False).order_by('kelas')
    students_tkj_3 = Siswa.objects.filter(kelas='XII.TKJ-3', pkl=False).order_by('kelas')
    students_tkj_4 = Siswa.objects.filter(kelas='XII.TKJ-4', pkl=False).order_by('kelas')
    instansi = Instansi.objects.all().order_by('nama')
    # for ins in instansi_temp:
      # filter instansi yang limit-nya kurang <= 5
      # instansi = Instansi.objects.filter(program_keahlian='RPL', slot__lt=ins.kuota).order_by('nama')
  return render(request, 'tambah-surat-permohonan.html', 
    {
      'students_rpl_1':students_rpl_1,
      'students_rpl_2':students_rpl_2,
      'students_rpl_3':students_rpl_3,
      'students_rpl_4':students_rpl_4,
      'students_tkj_1':students_tkj_1,
      'students_tkj_2':students_tkj_2,
      'students_tkj_3':students_tkj_3,
      'students_tkj_4':students_tkj_4,
      'instansi':instansi,
    }
  )


@login_required(login_url=settings.LOGIN_URL)
def tambah_surat_rpl(request):
  if request.POST:
    siswa = Siswa.objects.get(id=request.POST['nama_siswa'])
    instansi_temp = Instansi.objects.get(id=request.POST['nama_instansi'])
    Permohonan(
      nama_siswa = siswa,
      nama_instansi = instansi_temp,
    ).save()   

    # ubah status pkl siswa menjadi True
    Siswa.objects.filter(id=siswa.id).update(pkl=True) 

    # ubah limit slot instansi +1
    cur_slot = instansi_temp.slot + 1
    Instansi.objects.filter(id=instansi_temp.id).update(slot=cur_slot)

    msg = "Data berhasil ditambahkan."
    students_rpl_1 = Siswa.objects.filter(kelas='XII.RPL-1', pkl=False).order_by('kelas')
    students_rpl_2 = Siswa.objects.filter(kelas='XII.RPL-2', pkl=False).order_by('kelas')
    students_rpl_3 = Siswa.objects.filter(kelas='XII.RPL-3', pkl=False).order_by('kelas')
    students_rpl_4 = Siswa.objects.filter(kelas='XII.RPL-4', pkl=False).order_by('kelas')
    instansi_temp = Instansi.objects.filter(program_keahlian="RPL").order_by('nama')
    for ins in instansi_temp:
      # filter instansi, hanya menampilkan yang limit-nya <= kuota
      instansi = Instansi.objects.filter(program_keahlian='RPL', slot__lt=ins.kuota).order_by('nama')
    return render(request, 'tambah-surat-rpl.html', 
      {
        'msg':msg,
        'students_rpl_1':students_rpl_1,
        'students_rpl_2':students_rpl_2,
        'students_rpl_3':students_rpl_3,
        'students_rpl_4':students_rpl_4,
        'instansi':instansi,
      }
    )
  else:
    students_rpl_1 = Siswa.objects.filter(kelas='XII.RPL-1', pkl=False).order_by('kelas')
    students_rpl_2 = Siswa.objects.filter(kelas='XII.RPL-2', pkl=False).order_by('kelas')
    students_rpl_3 = Siswa.objects.filter(kelas='XII.RPL-3', pkl=False).order_by('kelas')
    students_rpl_4 = Siswa.objects.filter(kelas='XII.RPL-4', pkl=False).order_by('kelas')
    instansi = Instansi.objects.filter(program_keahlian="RPL").order_by('nama')
    # for ins in instansi_temp:
      # filter instansi yang limit-nya kurang <= 5
      # instansi = Instansi.objects.filter(program_keahlian='RPL', slot__lt=ins.kuota).order_by('nama')
  return render(request, 'tambah-surat-rpl.html', 
    {
      'students_rpl_1':students_rpl_1,
      'students_rpl_2':students_rpl_2,
      'students_rpl_3':students_rpl_3,
      'students_rpl_4':students_rpl_4,
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
    
    # ubah status pkl siswa menjadi True
    Siswa.objects.filter(id=siswa.id).update(pkl=True) 

    # ubah limit slot instansi +1
    cur_slot = instansi.slot + 1
    Instansi.objects.filter(id=instansi.id).update(slot=cur_slot)

    msg = "Data berhasil ditambahkan."
    students_tkj_1 = Siswa.objects.filter(kelas='XII.TKJ-1', pkl=False).order_by('kelas')
    students_tkj_2 = Siswa.objects.filter(kelas='XII.TKJ-2', pkl=False).order_by('kelas')
    students_tkj_3 = Siswa.objects.filter(kelas='XII.TKJ-3', pkl=False).order_by('kelas')
    students_tkj_4 = Siswa.objects.filter(kelas='XII.TKJ-4', pkl=False).order_by('kelas')
    instansi = Instansi.objects.filter(program_keahlian="TKJ").order_by('nama')
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
    instansi = Instansi.objects.filter(program_keahlian="TKJ").order_by('nama')
  return render(request, 'tambah-surat-tkj.html', 
    {
      'students_tkj_1':students_tkj_1,
      'students_tkj_2':students_tkj_2,
      'students_tkj_3':students_tkj_3,
      'students_tkj_4':students_tkj_4,
      'instansi':instansi,
    }
  )