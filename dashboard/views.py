from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from master.models import Siswa, Instansi

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
  students = Siswa.objects.all()
  students_rpl = Siswa.objects.filter(program_ahli='Rekayasa Perangkat Lunak').count()
  students_tkj = Siswa.objects.filter(program_ahli='Teknik Komputer dan Jaringan').count()

  ready_rpl = Siswa.objects.filter(program_ahli='Rekayasa Perangkat Lunak', pkl=True).count()
  ready_tkj = Siswa.objects.filter(program_ahli='Teknik Komputer dan Jaringan', pkl=True).count()

  students_count = len(students)

  return render(request, 'dashboard.html',
    {
      'students_count': students_count,
      'students_count_rpl': students_rpl,
      'students_count_tkj': students_tkj,

      'ready_rpl': ready_rpl,
      'ready_tkj': ready_tkj,
    }
  )