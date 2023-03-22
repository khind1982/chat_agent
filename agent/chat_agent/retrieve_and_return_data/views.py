import sys
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext

from retrieve_and_return_data.forms import LazyActiveForm

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from chat_agent_utils import retrieve_holiday_data

def retrieve_data(request):
    context = {}
    form = LazyActiveForm()
    context['form'] = form
    if request.method == 'POST':
        lazy = request.POST.getlist('lazy')
        active = request.POST.getlist('active')
        if lazy:
            results = retrieve_holiday_data([('lazy'), ('mild'), ('city')])
            context['results'] = reformat_database_results(results)
    return render(
        request, "chat_interface.html", context
    )


def reformat_database_results(results):
    reformatted_results = []
    for result in results:
        reformatted_result = {}
        city, price, country, hotel = result
        reformatted_result['city'] = city
        reformatted_result['price'] = price
        reformatted_result['country'] = country
        reformatted_result['hotel'] = hotel
        reformatted_results.append(reformatted_result)
    return reformatted_results
