from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Donation(models.Model):
    user = models.ForeignKey('Person',on_delete=models.CASCADE, default='')
    amount = models.IntegerField(default=0)
    card = models.CharField(max_length=30)
    card_num = models.IntegerField(default=0)

    
    def __str__(self):
        return str(self.user)



