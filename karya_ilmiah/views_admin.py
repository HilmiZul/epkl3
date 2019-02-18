from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import SubmissionJudul
from akun.models import AkunSiswa
from master.models import PembimbingSiswa, Siswa
from datetime import datetime


@login_required(login_url=settings.LOGIN_URL)
def pengajuan_judul(request):
  judul = SubmissionJudul.objects.filter(
    Q(pembimbing__pembimbing_satu__nama=request.session['nama']) | Q(pembimbing__pembimbing_dua__nama=request.session['nama']) 
  )
  return render(request, 'pengajuan-judul-pembimbing.html', {'judul':judul})

@login_required(login_url=settings.LOGIN_URL)
def pengajuan_judul_admin(request):
  judul = SubmissionJudul.objects.all().order_by('siswa__profil__kelas')
  return render(request, 'pengajuan-judul-admin.html', {'judul':judul})


@login_required(login_url=settings.LOGIN_URL)
def setuju_submission_judul(request, id):
  SubmissionJudul.objects.filter(id=id).update(
    tanggal_acc = datetime.now(),
    status = "Disetujui",
  )
  # ubah status judul di Siswa
  # ambil id siswa dulu, gimana caranya?
  # ambil data submissionjudul dari id yg disetujui
  # lalu ambil id_siswa dengan melakukan blusukan a.k.a relational mapping :D
  get_currnet_judul = SubmissionJudul.objects.get(id=id)
  id_siswa = get_currnet_judul.siswa.profil.id
  Siswa.objects.filter(id=id_siswa).update(status_judul=True)

  msg = "Judul berhasil disetujui."
  judul = SubmissionJudul.objects.filter(
    Q(pembimbing__pembimbing_satu__nama=request.session['nama']) | Q(pembimbing__pembimbing_dua__nama=request.session['nama']) 
  )
  # return render(request, 'show-submission-judul.html', {'judul':judul})
  return redirect('/karya-ilmiah/pengajuan-judul/')


@login_required(login_url=settings.LOGIN_URL)
def dikembalikan_submission_judul(request, id):
  get_judul = SubmissionJudul.objects.get(id=id)
  if get_judul.status == "Disetujui":
    msg = "Judul sudah disetujui. Tidak bisa diubah dan dikembalikan."
  else:
    SubmissionJudul.objects.filter(id=id).update(
      tanggal_acc = datetime.now(),
      status = "Ditolak",
    )
    msg = "Judul ditolak dan telah dikembalikan."
  judul = SubmissionJudul.objects.filter(
    Q(pembimbing__pembimbing_satu__nama=request.session['nama']) | Q(pembimbing__pembimbing_dua__nama=request.session['nama']) 
  )
  return render(request, 'show-submission-judul.html', {'judul':judul})