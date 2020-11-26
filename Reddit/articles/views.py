# ToDo: upload images
# ToDo: Search
# 3 ToDo: hashtag
# ToDo: custom 404
import json

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from account.models import User, Session
from .models import Article, Comment, Vote
from .service import *


vote = {
	"up":1,
	"down":-1
}


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
			article_votes = article.votes

			# make json
			response_data = {}
			response_data['text_label'] = article_text_label
			response_data['text'] = article_text
			response_data['pub_date'] = article_pub_date
			response_data['user_name'] = article_user_name
			response_data['vote'] = article_votes

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


def get_last_articles_handler(request):
	return JsonResponse(make_responce_last_articles())


def make_vote_handler(request, user_name, label_text):
	# check have we there user
	if Session.objects.filter(user_session = request.session["SessionForConfirmEmail"]):
		# get the user that make article
		article_user = User.objects.get(user_name = user_name)

		# cheking have this user there article
		if Article.objects.filter(user = article_user, text_label = label_text):
			# get the user and article
			user = Session.objects.get(user_session = request.session["SessionForConfirmEmail"]).user
			article = Article.objects.get(user = article_user, text_label = label_text)

			# get the vote
			votting = request.GET['vote']

			#cheking was this user make vote
			if Vote.objects.filter(article = article, user = user):
				if votting == "down" or votting == "up":
					# change the vote
					make_vote = Vote.objects.get(article = article, user = user)

					# change the numbers of votes
					article.votes += vote[make_vote.vote] * (-1) + vote[votting]
					article.save()

					make_vote.vote = votting
		
					make_vote.save()

					return HttpResponse("200")

				# delete a vote
				make_vote = Vote.objects.get(article = article, user = user)

				# change the numbers of votes
				article.votes += vote[make_vote.vote] * (-1)
				article.save()

				make_vote.delete()

				return HttpResponse("200")

			if votting == "down" or votting == "up":
				# make a new vote
				make_vote = Vote()

				make_vote.article = article
				make_vote.user = user
				make_vote.vote = votting

				make_vote.save()

				#change the numbers of votes
				article.votes += vote[votting]
				article.save()

				return  HttpResponse("200")

			return  HttpResponse("not right vote")

		return HttpResponse("we havent this article")

	return HttpResponse("You not register")


def most_vote_handler(request):
	return JsonResponse(make_responce_most_votes())


def have_user_vote_yet(request, user_name, label_text):
	"""This function is check vote this user yet"""
	session = request.session["SessionForConfirmEmail"]

	try:
		vote_yet = checking_vote_user_yet(session, user_name, label_text)

		return JsonResponse({'vote_yet':vote_yet})
	except:
		return JsonResponse({'eror':'we havent this article'})


def get_lent_handler(request):
	"""this function is making lent for user"""

	try:
		return JsonResponse(make_lent(num=5))
	except:
		return JsonResponse({'eror':'we havent your session'})