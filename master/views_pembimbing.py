from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pembimbing, PembimbingSiswa
from .form_pembimbing import FormPembimbing, FormPembimbingSiswa


@login_required(login_url=settings.LOGIN_URL)
def tambah_pembimbing(request):
  if request.POST:
    form = FormPembimbing(request.POST)
    if form.is_valid():
      form.save()
      msg = "Data Berhasil disimpan"
      form = FormPembimbing()
      return render(request, 'tambah-pembimbing.html', 
        {
          'msg':msg,
          'form':form,
        }
      )
  else:
    form = FormPembimbing()
  return render(request, 'tambah-pembimbing.html', {'form':form})


@login_required(login_url=settings.LOGIN_URL)
def pembimbing(request):
  pembimbing = Pembimbing.objects.all().order_by('jurusan')
  return render(request, 'pembimbing.html', {'pembimbing':pembimbing})


@login_required(login_url=settings.LOGIN_URL)
def ubah_pembimbing(request, id):
  if request.POST:
    Pembimbing.objects.filter(id=id).update(
      nama = request.POST['nama'],
      jurusan = request.POST['jurusan'],
    )
    msg = "Data berhasil diperbaharui."
    pembimbing = Pembimbing.objects.get(id=id)
    form = FormPembimbing()
    return render(request, 'ubah-pembimbing.html', 
      {
        'msg':msg,
        'pembimbing': pembimbing,
        'form': form,
      }
    )
  else:
    pembimbing = Pembimbing.objects.get(id=id)
    form = FormPembimbing()
  return render(request, 'ubah-pembimbing.html', 
    {
      'pembimbing':pembimbing,
      'form': form,
    }
  )


@login_required(login_url=settings.LOGIN_URL)
def hapus_pembimbing(request, id):
  Pembimbing.objects.filter(id=id).delete()
  msg = "Data berhasil dihapus."
  
  # update data setelah penghapusan
  pembimbing = Pembimbing.objects.all().order_by('jurusan')
  return render(request, 'pembimbing.html', 
    {
      'msg':msg,
      'pembimbing': pembimbing,
    }
  )


# PEMBIMBING.SISWA
@login_required(login_url=settings.LOGIN_URL)
def tambah_pembimbing_siswa(request):
  if request.POST:
    form = FormPembimbingSiswa(request.POST)
    if form.is_valid():
      form.save()
      msg = "Data Berhasil disimpan"
      form = FormPembimbingSiswa()
      return render(request, 'tambah-pembimbing-siswa.html', 
        {
          'msg':msg,
          'form':form,
        }
      )
  else:
    form = FormPembimbingSiswa()
  return render(request, 'tambah-pembimbing-siswa.html', {'form':form})

@login_required(login_url=settings.LOGIN_URL)
def pembimbing_siswa(request):
  ps = PembimbingSiswa.objects.all().order_by('siswa__kelas')
  return render(request, 'pembimbing-siswa.html', {'ps':ps})

@login_required(login_url=settings.LOGIN_URL)
def hapus_pembimbing_siswa(request, id):
  # hapus
  PembimbingSiswa.objects.filter(id=id).delete()
  msg = "Data berhasil dihapus."

  # update data setelah ada penghapusan
  ps = PembimbingSiswa.objects.all().order_by('siswa__kelas')
  return render(request, 'pembimbing-siswa.html', 
    {
      'msg': msg,
      'ps': ps,
    }
  )