from django.shortcuts import render

def timeline(request):
  template = 'jurnal_timeline.html'
  return render(request, template)
