from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import SubmissionJudul
from akun.models import AkunSiswa
from master.models import PembimbingSiswa
from datetime import datetime


@login_required(login_url=settings.LOGIN_URL)
def show_submission_judul(request):
  judul = SubmissionJudul.objects.filter(
    Q(pembimbing__pembimbing_satu__nama=request.session['nama']) | Q(pembimbing__pembimbing_dua__nama=request.session['nama']) 
  )
  return render(request, 'show-submission-judul.html', {'judul':judul})


@login_required(login_url=settings.LOGIN_URL)
def setuju_submission_judul(request, id):
  SubmissionJudul.objects.filter(id=id).update(
    tanggal_acc = datetime.now(),
    status = "Disetujui",
  )
  msg = "Judul berhasil disetujui."
  judul = SubmissionJudul.objects.filter(
    Q(pembimbing__pembimbing_satu__nama=request.session['nama']) | Q(pembimbing__pembimbing_dua__nama=request.session['nama']) 
  )
  return render(request, 'show-submission-judul.html', {'judul':judul})


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