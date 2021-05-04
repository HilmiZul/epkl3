from django.shortcuts import render, redirect
from .models import Siswa, Instansi, Pembimbing
from letter.models import Permohonan
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form_instansi import FormTambahInstansi

@login_required(login_url=settings.LOGIN_URL)
def get_master_peserta(request):
  data = Siswa.objects.all().order_by('NIS')
  template = 'master-peserta.html'
  context = {
    'data': data
  }
  return render(request, template, context)


@login_required(login_url=settings.LOGIN_URL)
def get_master_instansi(request):
  data = Instansi.objects.all().order_by('nama')
  template = 'master-instansi.html'
  context = {
    'data': data
  }
  return render(request, template, context)


@login_required(login_url=settings.LOGIN_URL)
def master_tambah_instansi(request):
  if request.POST:
    form = FormTambahInstansi(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Data berhasil disimpan")
      return redirect('tambah_instansi')
  else:
    form = FormTambahInstansi()
    context = {
      'form': form,
    }
  return render(request, 'tambah-instansi.html', context)


@login_required(login_url=settings.LOGIN_URL)
def master_ubah_instansi(request, id_instansi):
  if request.POST:
    Instansi.objects.filter(id=id_instansi).update(
      nama = request.POST['nama'],
      alamat = request.POST['alamat'],
      pimpinan = request.POST['pimpinan'],
      pembimbing = request.POST['pembimbing'],
      kontak = request.POST['kontak'],
      email = request.POST['email'],
      kuota = request.POST['kuota'],
      gender = request.POST['gender']
    )
    msg = "Data berhasil diperbaharui."
    messages.success(request, msg)
    return redirect('master_ubah_instansi',id_instansi)
  else:
    instansi = Instansi.objects.get(id=id_instansi)
    pkl = Permohonan.objects.filter(nama_instansi__id=id_instansi)
    context = {
      'instansi': instansi,
      'pkl': pkl
    }
  return render(request, 'ubah-instansi.html', context)


@login_required(login_url=settings.LOGIN_URL)
def master_hapus_instansi(request, id_instansi):
  Instansi.objects.filter(id=id_instansi).delete()
  msg = "Data berhasil dihapus."
  messages.success(request, msg)
  return redirect('get_master_instansi')