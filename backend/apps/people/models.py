from django.db import models
import collections
import json
from collections import defaultdict


class PersonManager(models.Manager):
	def has_full_info(self):
		#Only return those Person objects with non-blank values for both name and car_make
		return self.exclude(car_make=u'').exclude(name=u'')

	def cars_by_make(self):
		#returns all car makes, keyed to a list of owners (by ID) of those makes
		raw_data = defaultdict(list)
		for p in self.has_full_info():
			raw_data[p.car_make].append({p.id: p.name})
		response_data = []
		for make, owners in raw_data.iteritems():
			entry = {}
			entry['carMake'] = make
			entry['owners'] = owners
			response_data.append(entry)
		return json.dumps(response_data)

	def all_serialized(self):
		#JSON-serialized representation of all users with valid info
		response_data = []
		for p in self.has_full_info():
			entry = {}
			entry['name'] = p.name
			entry['carMake'] = p.car_make
			response_data.append(entry)
		return json.dumps(response_data)


class Person(models.Model):
    name = models.CharField(max_length=200, blank=True)
    car_make = models.CharField(max_length=200, blank=True)

    def serialize(self):
    	#Remember that this does not return a valid JSON object, but a small custom object
    	#with the owner's name keyed to their car make (Rather than [{name: self.name, make:self.car_make}])
    	#For a larger model or one where we were worried more about scaling, we'd make a true JSON serializer
    	return json.dumps({self.name: self.car_make})
    
    class Meta:
    	def __unicode__(self):
    		return self.name

    objects = PersonManager()	#implement our custom PersonManager manager