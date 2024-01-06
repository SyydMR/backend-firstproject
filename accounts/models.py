from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='user_pic', default='user_pic/nobody-face.jpg')
    phone = models.CharField(max_length=30, null=True)
    national_code = models.CharField(max_length=10, null=True)


    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "Users"