from asyncore import read
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from master.models import Siswa, Instansi, PembimbingSiswa
from letter.models import Permohonan
from karya_ilmiah.models import SubmissionJudul


def home(request):
  students = Siswa.objects.all()
  instansi = Instansi.objects.all().count()
  ready_pkl = Siswa.objects.filter(pkl=True).count()
  not_yet   = len(students) - ready_pkl
  students_count = len(students)

  prosentase_ready = (ready_pkl / students_count) * 100
  prosentase_ready = round(prosentase_ready, 2)

  prosentase_not_ready = (not_yet / students_count) * 100
  prosentase_not_ready = round(prosentase_not_ready, 2)

  ready = Permohonan.objects.all().order_by('nama_instansi')
  ready_rpl1 = Siswa.objects.filter(kelas__nama='XII.RPL-1', pkl=True).count()
  count_rpl1 = Siswa.objects.filter(kelas__nama='XII.RPL-1').count()
  ready_rpl2 = Siswa.objects.filter(kelas__nama='XII.RPL-2', pkl=True).count()
  count_rpl2 = Siswa.objects.filter(kelas__nama='XII.RPL-2').count()
  ready_rpl3 = Siswa.objects.filter(kelas__nama='XII.RPL-3', pkl=True).count()
  count_rpl3 = Siswa.objects.filter(kelas__nama='XII.RPL-3').count()

  prosentase_ready_rpl1 = (ready_rpl1 / count_rpl1) * 100
  prosentase_ready_rpl1 = round(prosentase_ready_rpl1, 2)
  prosentase_ready_rpl2 = (ready_rpl2 / count_rpl2) * 100
  prosentase_ready_rpl2 = round(prosentase_ready_rpl2, 2)
  prosentase_ready_rpl3 = (ready_rpl3 / count_rpl3) * 100
  prosentase_ready_rpl3 = round(prosentase_ready_rpl3, 2)
  return render(request, 'home.html',
    {
      'jumlah_peserta': students_count,
      'jumlah_instansi': instansi,
      'ready_pkl': ready_pkl,
      'not_yet': not_yet,
      'prosentase_ready': prosentase_ready,
      'prosentase_not_ready': prosentase_not_ready,
      'ready': ready,
      'ready_rpl1': ready_rpl1,
      'ready_rpl2': ready_rpl2,
      'ready_rpl3': ready_rpl3,
      'prosentase_ready_rpl1': prosentase_ready_rpl1,
      'prosentase_ready_rpl2': prosentase_ready_rpl2,
      'prosentase_ready_rpl3': prosentase_ready_rpl3
    }
  )

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
  students = Siswa.objects.all()
  instansi = Instansi.objects.all().count()
  students_rpl = Siswa.objects.filter(program_ahli__nama='RPL').count()

  ready_rpl = Siswa.objects.filter(program_ahli__nama='RPL', pkl=True).count()
  ready_pkl = ready_rpl
  not_yet   = len(students) - ready_pkl

  students_count = len(students)

  return render(request, 'dashboard.html',
    {
      'students_count': students_count,
      'students_count_rpl': students_rpl,
      'instansi': instansi,

      'ready_rpl': ready_rpl,
      'ready_pkl': ready_pkl,
      'not_yet': not_yet,
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
