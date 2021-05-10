from django.shortcuts import render


# Create your views here.
from django.template import loader


def home(request):
    return render(request, template_name='base.html')
