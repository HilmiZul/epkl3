from django.contrib import admin
from .models import Jurnal

class JurnalAdmin(admin.ModelAdmin):
  list_display  = ['siswa', 'pembimbing', 'tanggal', 'verify', 'status']
  list_filter   = ('verify', 'status',)
  search_fields = ['siswa', 'pembimging']
  list_per_page = 30


admin.site.register(Jurnal, JurnalAdmin)
