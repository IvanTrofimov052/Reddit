from .models import UserThatConfirmEmail, User
import re


# this function is checking the email adress
def checking_email_adress(email):
	# cheking if this email we have in our db
	if UserThatConfirmEmail.objects.filter(user_email = email) or User.objects.filter(user_email = email):
		return False

	match = re.search('@', email)

	return bool(match)

# this function cheked the age of user
def checking_age_of_user(age): 
	# checkinfd if user write the age not as number
	if age.isdigit() == False:
		return False

	# the user need to be more than ten years old
	if int(age) < 10:
		return False

	return True


# this function is cheking the user name of user
def checking_name_of_user(name):
	# cheking if this user name we have in our db
	if UserThatConfirmEmail.objects.filter(user_name = name) or User.objects.filter(user_name = name):
		return False

	return True