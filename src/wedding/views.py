from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

context = {
    'title': 'Wedding',
}

def index(request):
    return render(request, 'wedding/index.html', { 'page_to_load': 'wedding/home.html' } )

def accomodations(request):
    return render(request, 'wedding/index.html', { 'subpage': 'true', 'page_to_load': 'wedding/accommodations.html' } )
