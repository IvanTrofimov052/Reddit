from django.db import models


class UserThatConfirmEmail(models.Model):
	user_session = models.CharField(max_length=100)
	user_age = models.IntegerField(default=0)
	user_name = models.CharField(max_length=50)
	user_email = models.CharField(max_length=50)
	user_password = models.CharField(max_length=100)
	number_attempts = models.IntegerField(default=0)
	confirm_code = models.CharField(max_length=4)


class User(models.Model):
	user_age = models.IntegerField(default=0)
	user_name = models.CharField(max_length=50)
	user_email = models.CharField(max_length=50)
	user_password = models.CharField(max_length=100)


class Session(models.Model):
	user_session =  models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)