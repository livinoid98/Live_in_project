from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital

def index(request):
    hospitals = Hospital.objects
    return render(request, 'find/index.html', {'hospitals': hospitals})