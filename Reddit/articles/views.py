# ToDo: get all comments
import json

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from account.models import User, Session
from .models import Article, Comment


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

			# get information about article
			article_text = article.text
			article_text_label = article.text_label
			article_pub_date = article.pub_date
			article_user_name = article.user.user_name

			# make json
			response_data = {}
			response_data['text_label'] = article_text_label
			response_data['text'] = article_text
			response_data['pub_date'] = article_pub_date
			response_data['user_name'] = article_user_name

			return JsonResponse(response_data)

	return HttpResponse('we havent this article')


def make_comment_handler(request, user_name, label_text):
	# check have we there user
	if Session.objects.filter(user_session = request.session["SessionForConfirmEmail"]):
		# get the user
		user =  User.objects.get(user_name = user_name)

		# cheking have this user there article
		if Article.objects.filter(user = user, text_label = label_text):
			# get the user
			comment_user = Session.objects.get(user_session = request.session["SessionForConfirmEmail"]).user

			# get the comment text
			comment_text = request.GET['comment_text']

			# get the article
			comment_article = Article.objects.get(user = user, text_label = label_text)

			# get the today date
			comment_pub_date = datetime.now()

			# save this comment to db
			new_comment = Comment()
			new_comment.user = comment_user
			new_comment.comment_text = comment_text
			new_comment.article = comment_article
			new_comment.pub_date = comment_pub_date

			new_comment.save()

			return HttpResponse("OK")

		return HttpResponse('we havent this article')

	return HttpResponse('we havent this user')


def get_all_comments_of_article_handler(request, user_name, label_text):
	# get the user
	user = User.objects.get(user_name = user_name)

	if Article.objects.filter(user = user, text_label = label_text):
		# get this article
		article = Article.objects.get(user = user, text_label = label_text)

		# get all comments
		all_comments = Comment.objects.filter(article = article)

		# make a responce data
		response_data = {}
		response_data["max_id"] = len(all_comments)

		for i in range(len(all_comments)):
			comment = all_comments[i]
			user_name = comment.user.user_name
			pub_date = comment.pub_date
			comment_text = comment.comment_text

			response_data[i + 1] = {}
			response_data[i + 1]['user_name'] = user_name
			response_data[i + 1]['pub_date'] = pub_date
			response_data[i + 1]['comment_text'] = comment_text

		return JsonResponse(response_data)		

	return HttpResponse("we havent this article")