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
