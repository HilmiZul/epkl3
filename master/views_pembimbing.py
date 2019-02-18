from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pembimbing, PembimbingSiswa, Siswa
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
  pembimbing = Pembimbing.objects.all().order_by('nama')
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
      Siswa.objects.filter(id=request.POST['siswa']).update(
        pembimbing = True
      )
      pembimbing = Pembimbing.objects.all().order_by('nama')
      siswa = Siswa.objects.filter(pembimbing=False).order_by('kelas')
      msg = "Data Berhasil disimpan"
      return render(request, 'tambah-pembimbing-siswa.html', 
        {
          'msg':msg,
          'siswa': siswa,
          'pembimbing': pembimbing
        }
      )
  else:
    pembimbing = Pembimbing.objects.all().order_by('nama')
    siswa = Siswa.objects.filter(pembimbing=False).order_by('kelas')
    form = FormPembimbingSiswa()
  return render(request, 'tambah-pembimbing-siswa.html', 
    {
      'siswa': siswa,
      'pembimbing': pembimbing
    }
  )

@login_required(login_url=settings.LOGIN_URL)
def pembimbing_siswa(request):
  ps = PembimbingSiswa.objects.all().order_by('siswa__kelas')
  return render(request, 'pembimbing-siswa.html', {'ps':ps})

# FUNC.HAPUS.DATA.PEMBIMBING.SISWA
# MENERIMA id PembimbingSiswa
@login_required(login_url=settings.LOGIN_URL)
def hapus_pembimbing_siswa(request, id):
  # ambil id siswa dari pembimbin siswa sebelum dihapus
  pembimbing = PembimbingSiswa.objects.get(id=id)
  # ubah status pembimbing siswa menjadi false
  Siswa.objects.filter(id=pembimbing.siswa.id).update(pembimbing=False)
  
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

# UBAH.DATA.PEMBIMBING.SISWA
# MENERIMA id PembimbingSiswa
# @login_required(login_url=settings.LOGIN_URL)
# def ubah_pembimbing_siswa(request, id):
#   if request.POST:
#     # ambil data dari FK.
#     # masing-masing data referensi (dari Pembimbing & Siswa) untuk update data ke PembimbingSiswa
#     get_pembimbing = Pembimbing.objects.get(id=request.POST['pembimbing'])
#     get_siswa = Siswa.objects.get(id=request.POST['siswa'])

#     PembimbingSiswa.objects.filter(id=id).update(
#       pembimbing = get_pembimbing.id,
#       siswa = get_siswa.id,
#     )
#     msg = "Data berhasil diperbaharui."

#     # ubah status pembimbing siswa kalau siswa diubah 
#     if get_siswa:
#       pass

#     # update data yang telah diubah.
#     pembimbing = PembimbingSiswa.objects.get(id=id)
#     pembimbing_jamak = PembimbingSiswa.objects.filter(id=id)
#     siswa = Siswa.objects.all().order_by('kelas')
#     return render(request, 'ubah-pembimbing-siswa.html', 
#       {
#         'msg': msg,
#         'pembimbing': pembimbing,
#         'pembimbing_jamak': pembimbing_jamak,
#         'siswa': siswa
#       }
#     )
#   else:
#     pembimbing_jamak = PembimbingSiswa.objects.filter(id=id)
#     pembimbing = PembimbingSiswa.objects.get(id=id)
#     siswa = Siswa.objects.all().order_by('kelas')
#   return render(request, 'ubah-pembimbing-siswa.html', 
#     {
#       'pembimbing_jamak': pembimbing_jamak,
#       'pembimbing': pembimbing,
#       'siswa': siswa
#     })