from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Instansi

@login_required(login_url=settings.LOGIN_URL)
def ubah_instansi_rpl(request, id_instansi):
  if request.POST:
    Instansi.objects.filter(id=id_instansi).update(
      nama = request.POST['nama'],
      alamat = request.POST['alamat'],
    )
    msg = "Data berhasil diperbaharui."
    instansi = Instansi.objects.get(id=id_instansi)
    return render(request, 'ubah-instansi-rpl.html', 
      {
        'msg':msg, 
        'instansi':instansi, 
      }
    )
  else:
    instansi = Instansi.objects.get(id=id_instansi)
  return render(request, 'ubah-instansi-rpl.html', {'instansi':instansi})


@login_required(login_url=settings.LOGIN_URL)
def ubah_instansi_tkj(request, id_instansi):
  if request.POST:
    Instansi.objects.filter(id=id_instansi).update(
      nama = request.POST['nama'],
      alamat = request.POST['alamat'],
    )
    msg = "Data berhasil diperbaharui."
    instansi = Instansi.objects.get(id=id_instansi)
    return render(request, 'ubah-instansi-tkj.html', {'instansi':instansi})
  else:
    instansi = Instansi.objects.get(id=id_instansi)
  return render(request, 'ubah-instansi-tkj.html', {'instansi':instansi})