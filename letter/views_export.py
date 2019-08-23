import xlwt
from django.http import HttpResponse
from .models import Permohonan

def export_instansi_rpl(request):
  response = HttpResponse(content_type='application/ms-excel')
  response['Content-Disposition'] = 'attachment; filename="Daftar-Instansi-dan-Siswa-RPL.xls"'

  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet('Instansi & Siswa')

  # sheet header, first row
  row_num = 0

  font_style = xlwt.XFStyle()
  font_style.font.bold = True

  columns = ['Nama', 'Kelas', 'Instansi', 'Alamat', 'Keterangan']

  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)

  # sheet body, remaining rows
  font_style = xlwt.XFStyle()
  
  rows = Permohonan.objects.filter(nama_siswa__program_ahli='Rekayasa Perangkat Lunak').order_by('nama_instansi__nama', 'nama_siswa__nama').values_list(
          'nama_siswa__nama', 'nama_siswa__kelas', 'nama_instansi__nama', 'nama_instansi__alamat'
          )
  for row in rows:
    row_num = row_num + 1
    for col_num in range(len(row)):
      ws.write(row_num, col_num, row[col_num], font_style)

  wb.save(response)
  return response


def export_instansi_tkj(request):
  response = HttpResponse(content_type='application/ms-excel')
  response['Content-Disposition'] = 'attachment; filename="Daftar-Instansi-dan-Siswa-TKJ.xls"'

  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet('Instansi & Siswa')

  # sheet header, first row
  row_num = 0

  font_style = xlwt.XFStyle()
  font_style.font.bold = True

  columns = ['Nama', 'Kelas', 'Instansi', 'Alamat', 'Keterangan']

  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)

  # sheet body, remaining rows
  font_style = xlwt.XFStyle()
  
  rows = Permohonan.objects.filter(nama_siswa__program_ahli='Teknik Komputer dan Jaringan').order_by('nama_instansi__nama', 'nama_siswa__nama').values_list(
          'nama_siswa__nama', 'nama_siswa__kelas', 'nama_instansi__nama', 'nama_instansi__alamat'
          )
  for row in rows:
    row_num = row_num + 1
    for col_num in range(len(row)):
      ws.write(row_num, col_num, row[col_num], font_style)

  wb.save(response)
  return response