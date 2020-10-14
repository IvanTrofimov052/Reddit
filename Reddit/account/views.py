# dont forgot to change get to post
# to do the changing of making account
# to do checking the data
# to do method of making the accounts in othere function
# to do collect the image
# to do pep8
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def sign_up_handler(request):
	methond_of_creating_account = request.GET['methond_of_creating_account']

	# there we getting information about user
	user_age = request.GET['user_age']
	user_name = request.GET['user_name']
	user_password = request.GET['user_password']

	# there we checking the methond of creating account
	if methond_of_creating_account == "email":
		user_email = request.GET['user_email']
	else:
		return HttpResponse('Hacker!!!!!')

	return HttpResponse(user_email + '</br>' + user_age + '</br>' + user_name)
