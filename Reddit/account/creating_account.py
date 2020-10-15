# dont forgot about xss in the nickname
# to do creating new seesion
# to do send code to email
# to save code with data in db
from .checking import *
import uuid


# this function need to create account with your email
def creating_account_with_email_handler(request):
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

	return request.session["SessionForConfirmEmail"]
