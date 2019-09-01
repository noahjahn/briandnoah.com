from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

context = {
    'title': 'Wedding',
}

def index(request):
    return render(request, 'wedding/index.html')
