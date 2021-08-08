from django.contrib import admin
from donation.models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('user','amount','create_dt')