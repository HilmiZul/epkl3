from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .models import AkunSiswa

def masuk_siswa(request):
  if request.POST:
    user = authenticate(username=request.POST['uname'], password=request.POST['passwd'])
    if user is not None:
      if user.is_active:
        try:
          akun = AkunSiswa.objects.get(username=user.id)
          login(request, user)

          # bikin sesi
          request.session['uname'] = request.POST['uname']
          request.session['nama'] = akun.profil.nama
          request.session['id'] = akun.id
          request.session['id_siswa'] = akun.profil.id
        except:
          messages.add_message(request, messages.INFO, 'Login Gagal :(')
        return redirect('/')
      else:
        messages.add_message(request, message.INFO, 'User tidak terdaftar :(')
    else:
      messages.add_message(request, messages.INFO, 'Login gagal')
  return render(request, 'login-siswa.html')

@login_required(login_url=settings.LOGIN_URL)
def keluar_siswa(request):
  logout(request)
  return redirect('/siswa/login')