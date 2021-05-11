from urllib.parse import quote_plus
import requests
from django.shortcuts import render
from . import models
from bs4 import BeautifulSoup
import re
# Create your views here.
from django.template import loader

BASE_CRAIGSLIST_URL = 'https://delhi.craigslist.org/d/all/search/?query={}'


def home(request):
    return render(request, template_name='base.html')


def new_search(request):
    # Get the search block from the form
    search = request.POST.get('search')
    # Add the search to the database
    models.Search.objects.create(search=search)
    # Create the final request url for search
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    # Get the response from the craigslist website
    response = requests.get(final_url)
    # The html content
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    posts = soup.find_all('li', {'class': 'result-row'})

    details = []

    post_title = posts[0].find_all('a', {'class': 'result-title'})[0]  # This is the title
    post_price = posts[0].find_all('span', {'class': 'result-price'})[0]  # This is the price

    response2 = requests.get(post_title['href'])
    response2data = response2.text

    soup2 = BeautifulSoup(response2data, 'html.parser')
    image = soup2.find_all('img')[0]['src']

    details.append((post_title.text, post_price.text, image))

    # print(post_price)  # Title
    stuff_for_frontend = {
        'search': search,
        'details': details,
    }
    return render(request, template_name='my_app/new_search.html', context=stuff_for_frontend)
