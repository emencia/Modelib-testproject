from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('vote/<int:pk>/', views.VoteView.as_view(), name='vote'),
]
