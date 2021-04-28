from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Instansi
from django.contrib import messages
from .form_instansi import FormTambahInstansi
# from pesan import pesan


@login_required(login_url=settings.LOGIN_URL)
def tambah_instansi(request):
  if request.POST:
    form = FormTambahInstansi(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, msg)
      return redirect('tambah_instansi')
  else:
    form = FormTambahInstansi()
    context = {
      'form': form,
    }
  return render(request, 'tambah-instansi.html', context)


@login_required(login_url=settings.LOGIN_URL)
def tambah_instansi_rpl(request):
  if request.POST:
    Instansi(
      nama = request.POST['nama'],
      alamat = request.POST['alamat'],
      pimpinan = request.POST['pimpinan'],
      pembimbing = request.POST['pembimbing'],
      kontak = request.POST['kontak'],
      email = request.POST['email'],
      program_keahlian = "RPL",
      kuota = request.POST['kuota'],
      slot = 0,
      gender = request.POST['gender']
    ).save()
    msg = "Instansi berhasil ditambahkan."
    messages.success(request, msg)
    return redirect('tambah_instansi_rpl')
    # return render(request, 'tambah-instansi-rpl.html', {'msg':msg})
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
      program_keahlian = "TKJ",
      kuota = request.POST['kuota'],
      slot = 0,
      gender = request.POST['gender']
    ).save()
    msg = "Instansi berhasil ditambahkan."
    messages.success(request, msg)
    return redirect('tambah_instansi_tkj')
  return render(request, 'tambah-instansi-tkj.html')