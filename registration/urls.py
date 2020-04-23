from django.urls import path, re_path
from registration import views
from django.conf import settings


app_name = "registration"

urlpatterns = [
	re_path(r'^$', views.signup_view, name='signup_view'),
]


