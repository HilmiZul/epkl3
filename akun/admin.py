from django.contrib import admin
from .models import AkunPembimbing, AkunSiswa

# # Register your models here.
class AkunAdmin(admin.ModelAdmin):
    list_display = ['username', 'profil', 'level']
    search_fields = ['profil__nama', 'level']
    list_per_page = 20

class AkunSiswaAdmin(admin.ModelAdmin):
    list_display = ['username', 'profil']
    search_fields = ['profil__nama']
    list_per_page = 20

admin.site.register(AkunPembimbing, AkunAdmin)
admin.site.register(AkunSiswa, AkunSiswaAdmin)
