from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import SubmissionJudul
from akun.models import AkunSiswa
from master.models import PembimbingSiswa

@login_required(login_url=settings.LOGIN_URL)
def submission_judul(request):
  if request.POST:
    get_siswa = AkunSiswa.objects.get(id=request.session['id'])
    get_pembimbing = PembimbingSiswa.objects.get(siswa=get_siswa.profil)
    SubmissionJudul(
      judul = request.POST['judul'],
      submit_status = True,
      status = "Menunggu",
      siswa = get_siswa,
      pembimbing = get_pembimbing,
    ).save()
    msg = "Judul berhasil dikirim."
    judul = SubmissionJudul.objects.get(siswa__id=request.session['id'])
    return render(request, 'submission-judul.html', {'msg':msg, 'judul':judul})
  else:
    judul = SubmissionJudul.objects.get(siswa__id=request.session['id'])
  return render(request, 'submission-judul.html', {'judul':judul})


@login_required(login_url=settings.LOGIN_URL)
def show_submit_judul(request):
  judul = SubmissionJudul.objects.filter(siswa__id=request.session['id'])
  return render(request, 'judul.html', {'judul':judul})

@login_required(login_url=settings.LOGIN_URL)
def ubah_judul(request, id):
  if request.POST:
    SubmissionJudul.objects.filter(id=id).update(
      judul = request.POST['judul'],
      status = "Menunggu"
    )
    karil = SubmissionJudul.objects.get(siswa__id=request.session['id'])
    msg = "Judul telah diperbaharui dan dikirim ulang ke Pembimbing."
    return render(request, 'ubah-judul.html', {'msg':msg, 'karil':karil})
  else:
    karil = SubmissionJudul.objects.get(siswa__id=request.session['id'])
  return render(request, 'ubah-judul.html', {'karil':karil})