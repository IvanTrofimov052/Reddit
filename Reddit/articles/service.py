from account.models import User, Session
from .models import Article, Comment, Vote

from .random_functs import *


def get_user(user_name):
	# get the user
	user =  User.objects.get(user_name = user_name)

	return user


def get_article(user_name, label_text):
	user = get_user(user_name)

	# get article
	article = Article.objects.get(user = user, text_label = label_text)

	return article


def get_user_by_session(session):
	user = Session.objects.get(user_session = session).user
	return user


def checking_vote_user_yet(session, user_name, label_text):
	user = get_user_by_session(session)
	article = get_article(user_name, label_text)

	vote = bool(len(Vote.objects.filter(article = article, user = user)))

	if vote == True:
		return Vote.objects.get(article = article, user = user).vote

	return vote


def get_max_id_article():
	max_id = Article.objects.order_by('-id')[0].id

	return max_id

def get_Article_by_id(id):
	try:
		# get article
		article = Article.objects.get(id=id)

		return article
	except:
		return null


def get_information_about_article(article):
	response_data = {}

	article_text_label = article.text_label
	user_name = article.user.user_name
	pub_date = article.pub_date
	votes = article.votes

	response_data['text_label'] = article_text_label
	response_data['user_name'] = user_name
	response_data['pub_date'] = pub_date
	response_data['votes'] = votes

	return response_data


def make_information_about_articles_by_id(id_of_articles):
	response_data = {}
	response_data["max_id"] = len(id_of_articles)

	i=0

	for id in id_of_articles:
		article = get_Article_by_id(id)

		response_data[i+1] = get_information_about_article(article)

		i += 1

	return response_data


def make_lent(num=5):
	max_id = get_max_id_article()
	id_of_articles = random_non_repeating_nums(max_id, min(max_id, num))

	return make_information_about_articles_by_id(id_of_articles)
