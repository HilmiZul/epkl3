from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SubmissionJudul
from akun.models import AkunSiswa
from master.models import PembimbingSiswa

@login_required(login_url=settings.LOGIN_URL)
def submit_judul(request):
  get_siswa = AkunSiswa.objects.get(id=request.session['id'])
  get_pembimbing = PembimbingSiswa.objects.get(siswa=get_siswa.profil)
  if request.POST:
    SubmissionJudul(
      judul = request.POST['judul'],
      submit_status = True,
      status = "Menunggu",
      siswa = get_siswa,
      pembimbing = get_pembimbing,
      catatan = "",
    ).save()
    # msg = "Judul berhasil dikirim."
    # messages.add_message(request, messages.INFO, 'Judul berhasil dikirim.')
    # judul = SubmissionJudul.objects.get(siswa__id=request.session['id'])
    # return render(request, 'submit-judul.html', {'msg':msg, 'judul':judul})
    return redirect('/karya-ilmiah/judul')
  else:
    try:
      karil = SubmissionJudul.objects.get(siswa__id=request.session['id'])
      if karil.submit_status:
        redir = redirect('/karya-ilmiah/judul')
      else:
        redir = render(request, 'submit-judul.html')
    except:
      redir = render(request, 'submit-judul.html')
  return redir


@login_required(login_url=settings.LOGIN_URL)
def show_judul(request):
  karil = SubmissionJudul.objects.filter(siswa__id=request.session['id'])
  return render(request, 'judul.html', {'karil':karil})

@login_required(login_url=settings.LOGIN_URL)
def ubah_judul(request, id):
  if request.POST:
    SubmissionJudul.objects.filter(id=id).update(
      judul = request.POST['judul'],
      status = "Menunggu",
    )
    karil = SubmissionJudul.objects.get(siswa__id=request.session['id'])
    msg = "Judul telah diperbaharui dan dikirim ulang ke Pembimbing."
    return render(request, 'ubah-judul.html', {'msg':msg, 'karil':karil})
  else:
    karil = SubmissionJudul.objects.get(siswa__id=request.session['id'])
    # jika status sudah disetujui, judul haram diubah. :D
    if karil.status == 'Disetujui':
      return redirect('/karya-ilmiah/judul/')
    else:
      pass
  return render(request, 'ubah-judul.html', {'karil':karil})