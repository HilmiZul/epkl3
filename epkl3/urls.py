from django.contrib import admin
from django.urls import path, include
from dashboard.views import *
from django.conf import settings
from django.conf.urls.static import static
from akun.views_siswa import tambah_akun
from master.api_views import *
from letter.api_views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('siswa', SiswaViewset)
router.register('instansi', InstansiViewset)
router.register('permohonan', PermohonanViewset)


urlpatterns = [
    path('api/', include(router.urls)),

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

    #=====================
    # MASTER
    path('master/', include('master.urls_master')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)