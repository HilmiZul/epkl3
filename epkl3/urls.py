from django.contrib import admin
from django.urls import path, include
from dashboard.views import dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # akun
    path('akun/', include('akun.urls')),

    path('siswa/', include('akun.urls')),

    # dashboard
    path('', dashboard),
    path('dashboard/', include('dashboard.urls')),

    # instansi
    path('instansi/', include('master.urls_instansi')),

    # pkl & surat
    path('pkl/', include('letter.urls')),

    # pembimbing
    path('pembimbing/', include('master.urls_pembimbing')),

    # karya ilmiah
    # submission judul
    path('karya-ilmiah/', include('karya_ilmiah.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)