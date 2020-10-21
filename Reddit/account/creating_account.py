# dont forgot about xss in the nickname
# to do send code to email
# to do delting 
from .checking import *
import uuid
from .send_email import *
from .models import UserThatConfirmEmail
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import check_password, make_password
from .hash import *


# this function need to create account with your email
def creating_account_with_email_handler(request, user_password):
	# there we getting information about user
	user_age = request.GET['user_age']
	user_name = request.GET['user_name']
	user_email = request.GET['user_email']

	# there we cheking the information of user
	if checking_email_adress(user_email) == False:
		return "not working email adress"
	elif checking_name_of_user(user_name) == False:
		return "this nickname is busy"
	elif checking_age_of_user(user_age) == False:
		return "the age is not right"

	# making session with random values
	my_uuid = uuid.uuid4()
	request.session["SessionForConfirmEmail"] = str(my_uuid)

	# there we make aconfirmed code
	confirm_code = get_random_string(length=4, allowed_chars='1234567890')

	# there we sending email with code
	sending_email(user_email, str(confirm_code) + " your confirmation code")

	# thre we save that user
	new_user_that_confirm_email = UserThatConfirmEmail()
	new_user_that_confirm_email.user_session = request.session["SessionForConfirmEmail"]
	new_user_that_confirm_email.user_age = user_age
	new_user_that_confirm_email.user_name = user_name
	new_user_that_confirm_email.user_email = user_email
	new_user_that_confirm_email.user_password = hashing_passwords(user_password) # hash
	new_user_that_confirm_email.confirm_code  = confirm_code
	new_user_that_confirm_email.save()

	return "ok"
