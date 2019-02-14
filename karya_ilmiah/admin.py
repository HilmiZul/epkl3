from django.contrib import admin
from .models import SubmissionJudul

# Register your models here.
class SubmissionJudulAdmin(admin.ModelAdmin):
  list_display = ['judul', 'tanggal', 'tanggal_acc', 'submit_status', 'status', 'siswa', 'pembimbing']
  list_filter = ('submit_status', 'status',)
  search_fields = ['judul', 'siswa', 'pembimbing']
  list_per_page = 20


admin.site.register(SubmissionJudul, SubmissionJudulAdmin)