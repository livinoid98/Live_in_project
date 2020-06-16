from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Hospital, Review
from .forms import ReviewForm

def index(request):
    hospitals = Hospital.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        hospitals = hospitals.filter(name__contains=keyword)
    return render(request, 'find/index.html', {'hospitals': hospitals})

def detail(request, hospital_id):
    hospital = get_object_or_404(Hospital, pk=hospital_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.Hospital_id = hospital
            review.score = form.cleaned_data['score']
            review.content = form.cleaned_data['content']
            review.save()
            return redirect('Hospital_detail', hospital_id)
    else:
        form = ReviewForm()
        return render(request, 'find/detail.html', {'hospital': hospital, 'form': form})
