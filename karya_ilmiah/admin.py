from django.contrib import admin
from .models import SubmissionJudul, Bimbingan

# Register your models here.
class SubmissionJudulAdmin(admin.ModelAdmin):
  list_display = ['judul', 'tanggal_acc', 'submit_status', 'status', 'siswa', 'verified_by']
  list_filter = ('submit_status', 'status',)
  search_fields = ['judul', 'siswa', 'pembimbing']
  list_per_page = 20


class BimbinganAdmin(admin.ModelAdmin):
  list_display = ['judul', 'bab', 'tanggal', 'status', 'verified_by']
  list_filter = ('status',)
  search_fields = ['judul']
  list_per_page = 20


admin.site.register(SubmissionJudul, SubmissionJudulAdmin)
admin.site.register(Bimbingan, BimbinganAdmin)
