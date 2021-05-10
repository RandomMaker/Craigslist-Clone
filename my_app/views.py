import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
# Create your views here.
from django.template import loader


def home(request):
    return render(request, template_name='base.html')


def new_search(request):
    search = request.POST.get('search')
    print(search)
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, template_name='my_app/new_search.html', context=stuff_for_frontend)
