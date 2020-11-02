from django.db import models
from account.models import User, Session


class Article(models.Model):
    text = models.TextField(max_length=20000)
    text_label = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')


class Comment(models.Model):
	comment_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
