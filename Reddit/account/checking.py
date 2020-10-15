import re


# this function is checking the email adress
def checking_email_adress(email):
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
def checking_name_of_user(age):
	return True