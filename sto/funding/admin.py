from django.contrib import admin
from funding.models import Funding, FundingInfo
# Register your models here.


@admin.register(FundingInfo)
class FundingInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','price','goal_price','end_date')

@admin.register(Funding)
class FundingAdmin(admin.ModelAdmin):
    list_display = ('funding_info','user',)
