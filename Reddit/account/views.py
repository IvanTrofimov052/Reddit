# dont forgot to change get to post
# to do the changing of making account
# to do checking the data
# to do method of making the accounts in othere function
# to do collect the image
# to do pep8
# to do asynco
# dont forgot about hash
from django.http import HttpResponse
from .creating_account import *
from .models import UserThatConfirmEmail, User
from django.contrib.auth.hashers import check_password, make_password


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
			new_user.user_session = user_session
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
	user_password = request.GET['user_password']

	# cheking if the session of user is busy
	if User.objects.filter(user_session = request.session["SessionForConfirmEmail"]):
		return HttpResponse('Your session is busy')

	# cheking have we there user
	if User.objects.filter(user_name = user_name):
		# getting the right password
		user = User.objects.get(user_name = user_name)
		right_password = user.user_password

		# checking the password
		if user.check_password(user_password):
			return HttpResponse('nice')
		else:
			return HttpResponse('not right password')

	return HttpResponse('We havent this user')