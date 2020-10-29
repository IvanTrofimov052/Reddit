from django.urls import path

from . import views

urlpatterns = [
    path('MakePost', views.make_post_handler, name='index'),
    # ex: GetArticle/IvanTroifmov052/CoolArticle
    path('GetArticle/<str:user_name>/<str:label_text>', views.get_article_handler, name='index'),
]