from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
