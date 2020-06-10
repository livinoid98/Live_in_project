from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Hospital, Review

def index(request):
    hospitals = Hospital.objects
    return render(request, 'find/index.html', {'hospitals': hospitals})

def detail(request, hospital_id):
    hospital = get_object_or_404(Hospital, pk=hospital_id)
    return render(request, 'find/detail.html', {'hospital': hospital})
