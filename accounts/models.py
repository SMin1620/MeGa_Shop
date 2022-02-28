from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'

    first_name = None
    last_name = None
    date_joined = None

    name = models.CharField('이름', max_length=100)
    profile_img = models.ImageField('프로필 이미지', null=True, blank=True, upload_to='accounts/profile_img/%Y/%m/%d',
                                    help_text='gif/png/jpg 이미지를 업로드해주세요.')

    gender = models.CharField('성별', max_length=4, blank=True, choices=GenderChoices.choices)

    created_at = models.DateTimeField('생성날짜', auto_now_add=True)
    modified_at = models.DateTimeField('수정날짜', auto_now=True)
