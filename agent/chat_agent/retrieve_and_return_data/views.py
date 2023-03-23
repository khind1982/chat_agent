import sys
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext

from retrieve_and_return_data.forms import LazyActiveForm
from retrieve_and_return_data.forms import TemperatureRatingForm
from retrieve_and_return_data.forms import LocationForm

from multi_form_view import MultiModelFormView

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from chat_agent_utils import retrieve_holiday_data

class RetrieveData(MultiModelFormView):
    form_classes = {
        'lazy_form' : LazyActiveForm,
        'climate_form' : TemperatureRatingForm,
        'location_form' : LocationForm
    }
    template_name = 'chat_interface.html'
    def get_success_url(self):
        return reverse('home')
    def forms_valid(self, forms):
        activity = forms['lazy_form'].save(commit=False)
        climate = forms['climate_form'].save(commit=False)
        location = forms['location_form'].save(commit=False)
        return super(RetrieveData, self).forms_valid(forms)
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())
    def post(self, request, **kwargs):
        context = {}
        lazy = request.POST.getlist('lazy')
        active = request.POST.getlist('active')
        cold = request.POST.getlist('cold')
        mild = request.POST.getlist('mild')
        hot = request.POST.getlist('hot')
        city = request.POST.getlist('city')
        mountain = request.POST.getlist('mountain')
        sea = request.POST.getlist('sea')
        request = render_database_request(lazy, active, cold, mild, hot, city, mountain, sea)
        results = retrieve_holiday_data(request)
        reformatted_results = reformat_database_results(results)
        if reformat_database_results(results):
            context['results'] = reformat_database_results(results)
        else:
            context['default'] = results[0]
        return self.render_to_response(context)


def render_database_request(lazy, active, cold, mild, hot, city, mountain, sea):
    request = []
    activity_options = {'lazy':lazy, 'active':active}
    for activity_option,value in activity_options.items():
        if value:
            request.append((activity_option))
    
    climate_options = {'cold':cold, 'mild':mild, 'hot':hot}
    for climate_option,value in climate_options.items():
        if value:
            request.append((climate_option))

    location_options = {'city':city, 'mountain':mountain, 'sea':sea}
    for location_option,value in location_options.items():
        if value:
            request.append((location_option))

    return request


def reformat_database_results(results):
    reformatted_results = []
    for result in results:
        reformatted_result = {}
        try:
            city, price, country, hotel = result
        except ValueError:
            return False
        reformatted_result['city'] = city
        reformatted_result['price'] = price
        reformatted_result['country'] = country
        reformatted_result['hotel'] = hotel
        reformatted_results.append(reformatted_result)
    return reformatted_results
