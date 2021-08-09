from django.db import models
from django.contrib.auth.models import User

class Donation(models.Model):
    choice_card = { 
        ('shinhan', '신한'),
        ('woori', '우리'),
        ('hana', '하나'),
        ('kB', '국민'),
    }   


    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True )
    amount = models.IntegerField("금액",default=0)
    card = models.CharField("카드사", max_length=10, choices = choice_card)
    card_num = models.IntegerField("카드번호",default=0)
    create_dt = models.DateField('CREATE DATE', auto_now_add=True,null=True, blank=True)
    def __str__(self):
        return str(self.user)
