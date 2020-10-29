# ToDo: get article
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from account.models import User, Session
from .models import Article


# this function handler the create post
def make_post_handler(request):
	if Session.objects.filter(user_session = request.session["SessionForConfirmEmail"]):
		# get the information about article
		text_label = request.GET['text_label']
		text = request.GET['text']

		# get this article to data base
		article = Article()
		article.text = text
		article.text_label = text_label
		article.user = Session.objects.get(user_session = request.session["SessionForConfirmEmail"]).user
		article.pub_date = datetime.now()

		# cheking have there user a article with the same name
		if Article.objects.filter(text_label = text_label, user = Session.objects.get(user_session = request.session["SessionForConfirmEmail"]).user):
			return HttpResponse("you have article with there name")

		# save this article
		article.save()

		return HttpResponse("Nice we made your article")

	return HttpResponse("you not login")


# in this function we get article
def get_article_handler(request, user_name, label_text):
	# chaking have we there article
	if User.objects.filter(user_name = user_name):
		# get the user
		user =  User.objects.get(user_name = user_name)

		# cheking have this user there article
		if Article.objects.filter(user = user, text_label = label_text):
			# get thare article
			article = Article.objects.get(user = user, text_label = label_text)

			return HttpResponse(article.text)

	return HttpResponse('we havent this article')