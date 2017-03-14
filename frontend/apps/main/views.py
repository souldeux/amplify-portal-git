from django.http import HttpResponse
from django.shortcuts import render
import json
import requests

def show_homepage(request):
	return render(request, 'index.html')

#Since we're communicating with localhost on a different port, direct AJAX calls break
#same-origin policy. We could use JSONP and implement callbacks, but that would also
#expose the API endpoints and ports in our HTML source. This is slightly less elegant,
#but probably more secure and efficient.
def load_from_api(endpoint):
	#Make a GET request to the provided endpoint (a FQDN) and return the JSON dump we get back
	#separate this out from the fetch_api_response method in case we ever want to use this
	#convenience function to make headless calls from the backend rather than requiring a request object
	return json.dumps(requests.get(endpoint).json())

def fetch_api_response(request):
	#respond to a request from the template, figure out what endpoint it wants to see, and pass it here
	querystringArg = request.GET.get("arg", None)
	targetURL = "http://localhost:8500/"
	if querystringArg is not None:
		targetURL += str(querystringArg)
	return HttpResponse(load_from_api(targetURL), content_type='application/json')

