from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_safe #restricts views to GET and HEAD requests only
from .models import Person
import json
from config.secret import ALLOWED_KEYS


"""
Expose a read-only RESTful API to the frontend, implementing the following endpoints:

1. index: listing of all serialized person objects (localhost/)
2. person detail: detail lookup by ID for any given Person object (localhost/<ID>)
3. cars by make: a listing of all car_makes keyed to lists of the people that own them
"""
		

@require_safe
def index(request):
	#Return a serialized JSON dump of all Person objects
	#Included for the sake of completeness, we don't actually use this anywhere
	return HttpResponse(Person.objects.all_serialized())

@require_safe
def detail(request, **kwargs):
	#Returns a little object representing a single owner, with their name keyed to their carMake
	#Not valid JSON, just a simplified representation since the model is so small
	person = get_object_or_404(Person, id=kwargs.get('ID'))
	return HttpResponse(person.serialize())

@require_safe
def cars_by_make(request):
	#Returns a JSON dump of all car_makes keyed to lists of the people that own them
	return HttpResponse(Person.objects.cars_by_make())