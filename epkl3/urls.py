from django.contrib import admin
from django.urls import path, include
from dashboard.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # akun
    path('akun/', include('akun.urls')),

    # dashboard
    path('', dashboard),
    path('dashboard/', include('dashboard.urls')),

    # instansi
    path('instansi/', include('master.urls_instansi')),

    # pkl & surat
    path('pkl/', include('letter.urls')),

    # pembimbing
    path('pembimbing/', include('master.urls_pembimbing')),
]
