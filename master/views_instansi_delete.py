from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Instansi

@login_required(login_url=settings.LOGIN_URL)
def hapus_instansi_rpl(request, id_instansi):
  # deletion...
  Instansi.objects.filter(id=id_instansi).delete()

  # update data baru setelah aksi hapus
  instansi = Instansi.objects.filter(grup='RPL').order_by('nama')
  msg = "Data berhasil dihapus."
  return render(request, 'instansi-rpl.html', 
    {
      'instansi':instansi,
      'msg':msg,
    }
  )


@login_required(login_url=settings.LOGIN_URL)
def hapus_instansi_tkj(request, id_instansi):
  # hapus...
  Instansi.objects.filter(id=id_instansi).delete()

  # update data setelah aksi hapus
  instansi = Instansi.objects.filter(grup='TKJ').order_by('nama')
  msg = "Data berhasil dihapus."
  return render(request, 'instansi-tkj.html', 
    {
      'instansi':instansi,
      'msg':msg,
    }
  )
  
