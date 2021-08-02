from django.contrib import admin
from donation.models import Person
from donation.models import Donation

admin.site.register(Person)
admin.site.register(Donation)