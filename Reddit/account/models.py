from django.db import models


class UserThatConfirmEmail(models.Model):
    user_age = models.IntegerField(default=0)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=100)