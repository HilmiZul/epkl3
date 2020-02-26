from django.contrib import admin
from django.urls import path, include
from dashboard.views import *
from django.conf import settings
from django.conf.urls.static import static
from akun.views_siswa import tambah_akun

urlpatterns = [
    # halaman depan e-PKL
    path('', home, name='home'),

    path('admin/', admin.site.urls),
    
    # akun
    path('akun/', include('akun.urls')),
    path('tambah-akun/', tambah_akun),

    path('siswa/', include('akun.urls')),

    # dashboard
    path('dashboard/', include('dashboard.urls')),

    # instansi
    path('instansi/', include('master.urls_instansi')),

    # pkl & surat
    path('pkl/', include('letter.urls')),

    # pembimbing
    path('pembimbing/', include('master.urls_pembimbing')),

    # karya ilmiah
    # submission judul
    path('portofolio/', include('karya_ilmiah.urls')),

    # jurnal
    path('jurnal/', include('jurnal.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)