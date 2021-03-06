from django.urls import path

from . import views

urlpatterns = [
    path('MakePost', views.make_post_handler, name='index'),
    # ex: GetArticle/IvanTroifmov052/CoolArticle
    path('GetArticle/<str:user_name>/<str:label_text>', views.get_article_handler, name='index'),
    # ex: MakeComment/IvanTroifmov052/CoolArticle
    path('MakeComment/<str:user_name>/<str:label_text>', views.make_comment_handler, name='index'),
    # ex: GetAllComments/IvanTroifmov052/CoolArticle
    path('GetAllComments/<str:user_name>/<str:label_text>', views.get_all_comments_of_article_handler, name='index'),
    path('LastArticles', views.get_last_articles_handler, name='index'),
    path('Vote/<str:user_name>/<str:label_text>', views.make_vote_handler, name='index'),
    path('MostVote', views.most_vote_handler, name='index'),
    path('VoteYet/<str:user_name>/<str:label_text>', views.have_user_vote_yet, name='index'),
    path('GetLent', views.get_lent_handler, name='index')
]