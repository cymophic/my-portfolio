from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexTest(request):
    return HttpResponse('<h1> Hello World. <h1>')

def index(request):
    return render(request, 'index.html')