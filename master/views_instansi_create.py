from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Instansi
# from pesan import pesan


@login_required(login_url=settings.LOGIN_URL)
def tambah_instansi(request):
  if request.POST:
    Instansi(
      nama = request.POST['nama'],
      alamat = request.POST['alamat'],
      pimpinan = request.POST['pimpinan'],
      kontak = request.POST['kontak'],
      email = request.POST['email'],
      grup = request.POST['grup'],
      limit = 0,
    ).save()
    # msg = pesan().add()
    msg = "Instansi berhasil ditambahkan."
    return render(request, 'tambah-instansi.html', {'msg':msg})
  return render(request, 'tambah-instansi.html')


@login_required(login_url=settings.LOGIN_URL)
def tambah_instansi_rpl(request):
  if request.POST:
    Instansi(
      nama = request.POST['nama'],
      alamat = request.POST['alamat'],
      pimpinan = request.POST['pimpinan'],
      kontak = request.POST['kontak'],
      email = request.POST['email'],
      grup = "RPL",
      limit = 0,
    ).save()
    msg = "Instansi berhasil ditambahkan."
    return render(request, 'tambah-instansi-rpl.html', {'msg':msg})
  return render(request, 'tambah-instansi-rpl.html')


@login_required(login_url=settings.LOGIN_URL)
def tambah_instansi_tkj(request):
  if request.POST:
    Instansi(
      nama = request.POST['nama'],
      alamat = request.POST['alamat'],
      pimpinan = request.POST['pimpinan'],
      kontak = request.POST['kontak'],
      email = request.POST['email'],
      grup = "TKJ",
      limit = 0,
    ).save()
    msg = "Instansi berhasil ditambahkan."
    return render(request, 'tambah-instansi-tkj.html', {'msg':msg})
  return render(request, 'tambah-instansi-tkj.html')