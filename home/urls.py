from django.urls import path, include

from . import views


app_name = 'home'

urlpatterns = [
    # index page
    path('', views.IndexView.as_view(), name='index'),
]