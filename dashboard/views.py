from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from master.models import Siswa, Instansi, PembimbingSiswa
from letter.models import Permohonan
from karya_ilmiah.models import SubmissionJudul


def home(request):
  return render(request, 'home.html')

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


@login_required(login_url=settings.LOGIN_URL)
def dashboard_siswa(request):
  pembimbing = ''
  student = ''
  portofolio = ''
  try:
    student = Permohonan.objects.get(nama_siswa__id=request.session['id_siswa'])
    pembimbing = PembimbingSiswa.objects.get(siswa__id=request.session['id_siswa'])
    portofolio = SubmissionJudul.objects.get(siswa__profil__id=request.session['id_siswa'])
  except:
    portofolio = None
  return render(request, 'dashboard-siswa.html', {
    'student':student,
    'pembimbing':pembimbing,
    'portofolio':portofolio
  })