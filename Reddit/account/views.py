# dont forgot to change get to post
# to do the changing of making account
# to do checking the data
# to do method of making the accounts in othere function
# to do collect the image
# to do pep8
# to do asynco
# dont forgot about hash
# to do normal hashing
from django.http import HttpResponse
from .creating_account import *
from .models import UserThatConfirmEmail, User, Session
from django.contrib.auth.hashers import check_password, make_password
from .hash import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def sign_up_handler(request):
	methond_of_creating_account = request.GET['methond_of_creating_account']

	# there we get the user password
	user_password = request.GET['user_password']

	# there we checking the methond of creating account
	if methond_of_creating_account == "email":
		return HttpResponse(creating_account_with_email_handler(request, user_password))
	else:
		return HttpResponse('Hacker!!!!!')


def confirm_code_handler(request):
	# getting the code
	writing_code = request.GET['confirm_code']

	# there we checking have we there user
	if UserThatConfirmEmail.objects.filter(user_session = request.session["SessionForConfirmEmail"]):
		# get this user
		user_that_confirm_code = UserThatConfirmEmail.objects.get(user_session = request.session["SessionForConfirmEmail"])

		# get the right code and number attemps
		confirm_code = user_that_confirm_code.confirm_code
		number_attempts = user_that_confirm_code.number_attempts

		# getting information about user
		user_session = user_that_confirm_code.user_session
		user_age = user_that_confirm_code.user_age
		user_name = user_that_confirm_code.user_name
		user_email = user_that_confirm_code.user_email
		user_password = user_that_confirm_code.user_password

		#checking if the user write not right code
		if confirm_code == writing_code:
			# creating new user
			new_user = User()
			new_user.user_age = user_age
			new_user.user_name = user_name
			new_user.user_email = user_email
			new_user.user_password = user_password
			new_user.save()

			# delete of confirming users
			user_that_confirm_code.delete()

			return HttpResponse("ok")

		# checking if this people is making a lot of attemps
		if number_attempts > 4:
			# delete user beause there more then 4 attemps it means that people not know yhe code
			user_that_confirm_code.delete()

			return HttpResponse('not right we block your account')
		else:
			# it was not right code attemps is rising
			user_that_confirm_code.number_attempts += 1
			user_that_confirm_code.save()

			return HttpResponse('not right')


	return HttpResponse('You havent register go SignUp and register')


def sign_in_handler(request):
	# getting information
	user_name = request.GET['user_name']
	user_password = hashing_passwords(request.GET['user_password'])

	try:
		# cheking if the session of user is busy
		if Session.objects.filter(user_session = request.session["SessionForConfirmEmail"]):
			return HttpResponse('Your session is busy')
	except:
		# cheking have we there user
		if User.objects.filter(user_name = user_name):
			# getting the right password
			user = User.objects.get(user_name = user_name)
			right_password = user.user_password

			# checking the password
			if user_password == right_password:
				# creting session
				my_uuid = uuid.uuid4()
				request.session["SessionForConfirmEmail"] = str(my_uuid)

				# creating new session
				new_session = Session(user = user,
				 			  user_session = request.session["SessionForConfirmEmail"])
				new_session.save()

				return HttpResponse('nice')
			else:
				return HttpResponse('not right password')

		return HttpResponse('We havent this user')


def sign_out_handler(request):
	# cheking have we there session
	if Session.objects.filter(user_session = request.session["SessionForConfirmEmail"]):
		# getting this user and then delete
		session = Session.objects.get(user_session = request.session["SessionForConfirmEmail"])
		session.delete()

		return HttpResponse('OK')

	return HttpResponse('We havent your session')


def change_password_handler(request):
	# getting new password
	new_password = request.GET['new_password']

	# cheking have we there session
	if Session.objects.filter(user_session = request.session["SessionForConfirmEmail"]):
		# get new user and update his password
		user = Session.objects.get(user_session = request.session["SessionForConfirmEmail"]).user
		user.user_password = hashing_passwords(new_password)
		user.save()

		return HttpResponse('OK')

	return HttpResponse('We havent your session')

