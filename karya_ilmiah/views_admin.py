from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import SubmissionJudul, Bimbingan
from akun.models import AkunSiswa
from master.models import PembimbingSiswa, Siswa
from datetime import datetime
from django.contrib import messages


@login_required(login_url=settings.LOGIN_URL)
def pengajuan_judul(request):
  # judul = SubmissionJudul.objects.filter(
  #   Q(pembimbing__pembimbing_satu__nama=request.session['nama']) | Q(pembimbing__pembimbing_dua__nama=request.session['nama']) 
  # )
  judul = SubmissionJudul.objects.filter(
    Q(pembimbing__pembimbing_satu__nama=request.session['nama']) 
  )
  return render(request, 'pengajuan-judul-admin.html', {'judul':judul})

@login_required(login_url=settings.LOGIN_URL)
def pengajuan_judul_admin(request):
  judul = SubmissionJudul.objects.all().order_by('siswa__profil__kelas')
  return render(request, 'pengajuan-judul-admin.html', {'judul':judul})


@login_required(login_url=settings.LOGIN_URL)
def setuju_submission_judul(request, id):
  if request.POST:
    SubmissionJudul.objects.filter(id=id).update(
      tanggal_acc = datetime.now(),
      status = "Disetujui",
      verified_by = request.session['id']
    )
    # ubah status judul di Siswa
    # ambil id siswa dulu, gimana caranya?
    # ambil data submissionjudul dari id yg disetujui
    # lalu ambil id_siswa dengan melakukan blusukan a.k.a relational mapping :D
    get_currnet_judul = SubmissionJudul.objects.get(id=id)
    id_siswa = get_currnet_judul.siswa.profil.id
    Siswa.objects.filter(id=id_siswa).update(status_judul=True)

    # judul = SubmissionJudul.objects.filter(
    #   Q(pembimbing__pembimbing_satu__nama=request.session['nama']) | Q(pembimbing__pembimbing_dua__nama=request.session['nama']) 
    # )
    judul = SubmissionJudul.objects.filter(
      Q(pembimbing__pembimbing_satu__nama=request.session['nama'])
    )
    # return render(request, 'show-submission-judul.html', {'judul':judul})
    messages.add_message(request, messages.INFO, 'Judul Portofolio telah disetujui.')
    return redirect('/portofolio/pengajuan-judul/')
  


@login_required(login_url=settings.LOGIN_URL)
def dikembalikan_submission_judul(request, id):
  get_judul = SubmissionJudul.objects.get(id=id)
  if request.POST:
    if get_judul.status == "Disetujui":
      msg = "Judul sudah disetujui. Tidak bisa diubah dan dikembalikan."
    else:
      if request.POST['catatan'] is not None:
        catatan = request.POST['catatan']
      else:
        catatan = "Tidak ada catatan."
      SubmissionJudul.objects.filter(id=id).update(
        tanggal_acc = datetime.now(),
        status = "Ditolak",
        catatan = catatan,
      )
      msg = "Judul ditolak dan telah dikembalikan."
    # judul = SubmissionJudul.objects.filter(
    #   Q(pembimbing__pembimbing_satu__nama=request.session['nama']) | Q(pembimbing__pembimbing_dua__nama=request.session['nama']) 
    # )
    judul = SubmissionJudul.objects.filter(
      Q(pembimbing__pembimbing_satu__nama=request.session['nama'])
    )
    messages.add_message(request, messages.INFO, 'Judul Portofolio telah dikembalikan/tolak.')
    return redirect('/portofolio/pengajuan-judul/')
  return render(request, 'pengajuan-judul-admin.html', {'judul':judul})
  
  
  
@login_required(login_url=settings.LOGIN_URL)
def bimbingan_isi(request):
  # contents = Bimbingan.objects.filter(
  #   Q(judul__pembimbing__pembimbing_satu__nama=request.session['nama']) | Q(judul__pembimbing__pembimbing_dua__nama=request.session['nama']) 
  # ).order_by('judul__siswa', 'status', '-bab')
  contents = Bimbingan.objects.filter(
    Q(judul__pembimbing__pembimbing_satu__nama=request.session['nama'])
  ).order_by('judul__siswa', 'status', '-bab')
  return render(request, 'bimbingan-isi.html', {'contents':contents})


@login_required(login_url=settings.LOGIN_URL)
def bimbingan_isi_revisi(request, id):
  if request.POST:
    Bimbingan.objects.filter(id=id).update(
      catatan = request.POST['catatan'],
      status = 'Revisi'
    )
    messages.add_message(request, messages.INFO, 'Berkas berhasil dikembalikan.')
    return redirect('/portofolio/bimbingan-isi/')
  return redirect('/portofolio/bimbingan-isi/')


@login_required(login_url=settings.LOGIN_URL)
def setujui_bimbingan_isi(request, id):
  if request.POST:
    Bimbingan.objects.filter(id=id).update(
      status = 'Selesai',
      verified_by = request.session['id']
    )
    messages.add_message(request, messages.INFO, 'Berkas telah disetujui.')
    return redirect('/portofolio/bimbingan-isi/')
  return redirect('/portofolio/bimbingan-isi/')