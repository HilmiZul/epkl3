from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .models import AkunPembimbing

# Create your views here.
def masuk(request):
  if request.POST:
    user = authenticate(username=request.POST['uname'], password=request.POST['passwd'])
    if user is not None:
      if user.is_active:
        try:
          akun = AkunPembimbing.objects.get(username=user.id)
          login(request, user)

          # bikin sesi
          request.session['uname'] = request.POST['uname']
          request.session['nama'] = akun.profil.nama
          request.session['jurusan'] = akun.profil.jurusan
          request.session['id'] = akun.id
          request.session['level'] = akun.level
        except:
          messages.add_message(request, messages.INFO, 'Login Gagal :(')
        return redirect('/')
      else:
        messages.add_message(request, message.INFO, 'User tidak terdaftar :(')
    else:
      messages.add_message(request, messages.INFO, 'Login gagal')
  return render(request, 'login.html')

@login_required(login_url=settings.LOGIN_URL)
def keluar(request):
  logout(request)
  return redirect('/akun/masuk')