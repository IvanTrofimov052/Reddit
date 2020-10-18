from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('SignUp', views.sign_up_handler, name='index'),
    path('SignUp/ConfirmCode', views.confirm_code_handler, name='index'),
    path('SignIn', views.sign_in_handler, name='index'),
]