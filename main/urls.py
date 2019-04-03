from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('car/<int:pk>', views.CarView.as_view(), name='car')
]
