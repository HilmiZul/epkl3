import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SubmissionJudul, Bimbingan
from akun.models import AkunSiswa
from master.models import PembimbingSiswa
from letter.models import Permohonan
from .forms import FormBimbingan
from django.core.files.storage import FileSystemStorage

@login_required(login_url=settings.LOGIN_URL)
def submit_judul(request):
  if request.POST:
    try:
      get_siswa = AkunSiswa.objects.get(id=request.session['id'])
      get_pembimbing = PembimbingSiswa.objects.get(siswa=get_siswa.profil)
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
    except:
      pass
    return redirect('/portofolio/timeline')
  else:
    try:
      karil = SubmissionJudul.objects.get(siswa__id=request.session['id'])
      if karil.submit_status or karil.status == 'Disetujui':
        redir = redirect('/portofolio/timeline')
      else:
        redir = render(request, 'submit-judul-new.html')
    except:
      error_pembimbing = True
      redir = render(request, 'submit-judul-new.html', {'errPembimbing':error_pembimbing})
  return redir


@login_required(login_url=settings.LOGIN_URL)
def show_timeline(request):
  persentase = ''
  belum_bimbingan = False
  selesai = False # inisialisasi dengan False dulu biar ga error pas ngelempar ke template
                  # selesai ini yang akan menentukan apakah 4 bab telah terselesaikan?!
  try:
    # judul karya ilmiah (sekarang jadi Portofolio)
    karil = SubmissionJudul.objects.get(siswa__id=request.session['id'])
    cek_judul = SubmissionJudul.objects.filter(siswa__id=request.session['id'], status='Disetujui').count()
    # isi
    contents = Bimbingan.objects.filter(judul__id=karil.id).order_by('-tanggal').order_by('status', '-bab')
    is_done = Bimbingan.objects.filter(judul__id=karil.id, status='Selesai').count()
    jumlah_bab_aja = Bimbingan.objects.filter(judul__id=karil.id).count()
    jumlah_bab = is_done + cek_judul
    
    # hitung persentase progress: judul dan isinya. total keseluruhan 5 tahapan yang harus diselesaikan siswa
    persentase = (jumlah_bab/5) * 100
    persentase = int(persentase)
    
    if jumlah_bab == 5:
      selesai = True
    if jumlah_bab_aja == 0:
        belum_bimbingan = True
    return render(request, 'timeline.html', {
      'karil':karil, 'contents':contents, 
      'selesai':selesai, 'persentase':persentase,
      'belum_bimbingan':belum_bimbingan
    })
  except:
    karil = None
    contents = None
  return render(request, 'timeline.html', {
    'karil':karil, 'contents':contents,
    'selesai':selesai, 'persentase':persentase,
    'belum_bimbingan':belum_bimbingan
  })

@login_required(login_url=settings.LOGIN_URL)
def ubah_judul(request, id):
  if request.POST:
    SubmissionJudul.objects.filter(id=id).update(
      judul = request.POST['judul'],
      status = "Menunggu",
    )
    karil = SubmissionJudul.objects.get(siswa__id=request.session['id'])
    msg = "Judul telah diperbaharui dan dikirim ulang ke Pembimbing."
    messages.add_message(request, messages.INFO, 'Judul berhasil disunting dan dikirim ulang.')
    return render(request, 'ubah-judul-new.html', {'msg':msg, 'karil':karil})
  else:
    karil = SubmissionJudul.objects.get(siswa__id=request.session['id'])
    # jika status sudah disetujui, judul haram diubah. :D
    if karil.status == 'Disetujui':
      return redirect('/portofolio/timeline/')
    else:
      pass
  return render(request, 'ubah-judul-new.html', {'karil':karil})


@login_required(login_url=settings.LOGIN_URL)
def bimbingan_submit(request):
  selesai = False
  portofolio = ''
  try:
    if request.POST:
      # form = FormBimbingan(request.POST)
      # form.save()
      berkas = request.FILES['berkas']
      Bimbingan(
        judul = SubmissionJudul.objects.get(id=request.POST['judul']),
        bab = request.POST['bab'],
        berkas = berkas,
        catatan = None
      ).save()
      # fs = FileSystemStorage()
      # fs.save('berkas/'+berkas.name, berkas)
      messages.add_message(request, messages.INFO, 'Berkas berhasil dikirim dan akan di-review oleh Pembimbing.')
      return redirect('/portofolio/timeline/')
    else:
      # form = FormBimbingan()
      # cek jumlah BAB yang udah di submit. kalau sudah 4 maka tidak bisa submit lagi.
      # tunggu proses review dari pembimbing
      portofolio = SubmissionJudul.objects.get(siswa__id=request.session['id'])
      karil = SubmissionJudul.objects.get(siswa__id=request.session['id'])
      jumlah_bab = Bimbingan.objects.filter(judul__id=karil.id).count()
      if jumlah_bab == 4:
        selesai = True
  except:
    pass
  return render(request, 'bimbingan-submit.html', {'portofolio':portofolio, 'selesai':selesai})


@login_required(login_url=settings.LOGIN_URL)
def bimbingan_submit_revisi(request,id):
  if request.POST:
    # hapus berkas lama
    try:
      berkas_lama = Bimbingan.objects.get(id=id)
      os.remove(berkas_lama.berkas.path)
      # upload yang baru
      berkas = request.FILES['berkas']
      # berkas = os.path.join(settings.MEDIA_ROOT, berkas)
      Bimbingan.objects.filter(id=id).update(
        berkas = berkas,
        status = 'Review'
      )
      # fs = FileSystemStorage()
      # fs.save('berkas/'+berkas.name, berkas)
      fs = FileSystemStorage()
      fs.save(berkas.name, berkas)
      messages.add_message(request, messages.INFO, 'Berkas berhasil dikirim dan akan di-review kembali oleh Pembimbing.')
      return redirect('/portofolio/timeline/')
    except:
      pass
  return redirect('/portofolio/timeline/')


@login_required(login_url=settings.LOGIN_URL)
def unduh_halaman_judul(request):
  judul = SubmissionJudul.objects.get(siswa__id=request.session['id'])
  DUDI = Permohonan.objects.get(nama_siswa__id=judul.siswa.profil.id)
  return render(request, 'template-judul.html', {'judul':judul, 'DUDI':DUDI})