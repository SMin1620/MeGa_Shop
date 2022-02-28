from django.db import models

from accounts.models import User


# Create your models here.
class Market(models.Model):
    name = models.CharField('마켓이름', max_length=100)
    site_url = models.URLField('마켓사이트 url')
    email = models.EmailField(max_length=100)
    master = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    reg_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)




