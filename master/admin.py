from django.contrib import admin
from .models import Siswa, Instansi, Pembimbing, PembimbingSiswa, KompetensiDasar


# Register your models here.
class SiswaAdmin(admin.ModelAdmin):
    list_display = ['NIS', 'nama', 'kelas', 'isRapotTuntas', 'pkl', 'pembimbing', 'status_judul']
    list_filter = ('kelas', 'program_ahli', 'isRapotTuntas', 'pkl', 'status_judul', 'pembimbing')
    search_fields = ['NIS', 'nama']
    list_per_page = 20

    actions = ['dapat_tempat_pkl', 'belum_dapat_tempat_pkl']

    def dapat_tempat_pkl(self,request,queryset):
        queryset.update(pkl=True)

    def belum_dapat_tempat_pkl(self,request,queryset):
        queryset.update(pkl=False)

class InstansiAdmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat', 'pembimbing', 'kontak', 'program_keahlian', 'kuota']
    search_fields = ['nama', 'alamat']
    list_per_page = 20

class PembimbingAdmin(admin.ModelAdmin):
    list_display = ['nama', 'jurusan']
    list_filter = ('jurusan',)
    search_fields = ['nama', 'jurusan']
    list_per_page = 20

class PembimbingSiswaAdmin(admin.ModelAdmin):
    list_display = ['pembimbing_satu', 'siswa']
    list_filter = ('siswa__kelas', 'siswa__program_ahli',)
    search_fields = ['pembimbing_satu', 'siswa']
    list_per_page = 20

class KDAdmin(admin.ModelAdmin):
    list_display = ['kode', 'nama', 'jurusan']
    list_filter = ('jurusan',)
    search_fields = ['kode', 'nama', 'jurusan']
    list_per_page = 20

admin.site.register(Siswa, SiswaAdmin)
admin.site.register(Instansi, InstansiAdmin)
admin.site.register(Pembimbing, PembimbingAdmin)
admin.site.register(PembimbingSiswa, PembimbingSiswaAdmin)
admin.site.register(KompetensiDasar, KDAdmin)
