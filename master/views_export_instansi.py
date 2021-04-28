import xlwt
from django.http import HttpResponse
from .models import Instansi
from .resources import InstansiResource

def export_instansi(request):
  instansi = InstansiResource()
  dataset = instansi.export()
  response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
  response['Content-Disposition'] = 'attachment; filename=Data-Instansi-PKL-2021.xls'
  return response

def export_instansi_rpl(request):
  response = HttpResponse(content_type='application/ms-excel')
  response['Content-Disposition'] = 'attachment; filename="Daftar-Instansi-RPL.xls"'

  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet('Daftar Instansi RPL')

  # sheet header, first row
  row_num = 0

  font_style = xlwt.XFStyle()
  font_style.font.bold = True

  columns = ['Nama', 'Alamat', 'Pimpinan', 'Kontak', 'Email', 'Slot']

  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)

  # sheet body, remaining rows
  font_style = xlwt.XFStyle()
  
  rows = Instansi.objects.filter(grup='RPL').values_list('nama', 'alamat', 'pimpinan', 'kontak', 'email', 'limit')
  for row in rows:
    row_num = row_num + 1
    for col_num in range(len(row)):
      ws.write(row_num, col_num, row[col_num], font_style)

  wb.save(response)
  return response


def export_instansi_tkj(request):
  response = HttpResponse(content_type='application/ms-excel')
  response['Content-Disposition'] = 'attachment; filename="Daftar-Instansi-TKJ.xls"'

  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet('Daftar Instansi TKJ')

  # sheet header, first row
  row_num = 0

  font_style = xlwt.XFStyle()
  font_style.font.bold = True

  columns = ['Nama', 'Alamat', 'Pimpinan', 'Kontak', 'Email', 'Slot']

  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)

  # sheet body, remaining rows
  font_style = xlwt.XFStyle()
  
  rows = Instansi.objects.filter(grup='TKJ').values_list('nama', 'alamat', 'pimpinan', 'kontak', 'email', 'limit')
  for row in rows:
    row_num = row_num + 1
    for col_num in range(len(row)):
      ws.write(row_num, col_num, row[col_num], font_style)

  wb.save(response)
  return response