from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Hospital, Review

def index(request):
    hospitals = Hospital.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        hospitals = hospitals.filter(name__contains=keyword)
    return render(request, 'find/index.html', {'hospitals': hospitals})

def detail(request, hospital_id):
    hospital = get_object_or_404(Hospital, pk=hospital_id)
    return render(request, 'find/detail.html', {'hospital': hospital})
