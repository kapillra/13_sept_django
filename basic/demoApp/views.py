from django.shortcuts import render, redirect
from django.http import HttpResponse
from .myform import *
from .models import *

# Create your views here.

def index(request):
    return HttpResponse("<h1>first response</h1>")

def html_page(request):
    data = {
        'name': 'demo app',
        'tech': ['django', 'python', 'sql'],
        'form': Login()
    }
    return render(request, "index.html", data)

def get_form_data_and_save(request):
    print(request.POST)

    Master.objects.create(Name=request.POST['fullname'], Email = request.POST['email']) #ORM - object relational mapping

    # master = Master()

    # master.Name = request.POST['fullname']
    # master.Email = request.POST['email']

    # master.save()

    return redirect(html_page)