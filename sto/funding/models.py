from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime 
from django.conf import settings
# Create your models here.

class FundingInfo(models.Model):
    # 마감날짜, 목표금액, 서포터????, 
    title = models.CharField(max_length=200)
    end_date = models.DateTimeField(blank=True, null=True)
    goal_price = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_funding", blank=True)
    
    def __str__(self):
        return self.title

#  1000 x 100(%)
# 10000 
class Funding(models.Model):
    choice_card = { 
        ('shinhan', '신한'),
        ('woori', '우리'),
        ('hana', '하나'),
        ('kB', '국민'),
    }   
    choice_color = { 
        ('nougat', 'nougat 누가'),
        ('stormy', 'stormy 스토미'),
        ('pompom', 'pompom 폼폼'),
        ('milk', 'milk 밀크'),
    }

    user = models.ForeignKey(User,on_delete=models.CASCADE,
        verbose_name='USER', blank=True, null=True)
    funding_info = models.ForeignKey(FundingInfo,on_delete=models.CASCADE,
        verbose_name='Funding Info.', blank=True, null=True)
    cash = models.IntegerField(default=0)
    card = models.CharField("카드사", max_length=10, choices = choice_card, default='')
    card_num = models.IntegerField("카드번호",default=0)
    create_dt = models.DateField('CREATE DATE', auto_now_add=True,null=True, blank=True)
    color =models.CharField("색상", max_length=10, choices = choice_color, default='')
    
    class Meta:
        ordering = ('-cash',)
    # def get_absolute_url(self):
    #     return reverse('funding:funding_detail', args=(self.id,))
