from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime 
# Create your models here.

class FundingInfo(models.Model):
    # 마감날짜, 목표금액, 서포터????, 
    title = models.CharField(max_length=200)
    end_date = models.DateTimeField(blank=True, null=True)
    goal_price = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title

#  1000 x 100(%)
# 10000 
class Funding(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,
    verbose_name='USER', blank=True, null=True)
    funding_info = models.ForeignKey(FundingInfo,on_delete=models.CASCADE,
    verbose_name='Funding Info.', blank=True, null=True)
    cash = models.IntegerField(default=0)
    
    
    

    # def get_absolute_url(self):
    #     return reverse('funding:funding_detail', args=(self.id,))


