from import_export import resources
from .models import Instansi

class InstansiResource(resources.ModelResource):
  class Meta:
    model = Instansi
    exclude = ['program_keahlian']