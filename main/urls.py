from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('car/<int:pk>', views.CarView.as_view(), name='car'),
    path('car/create/', views.CarCreateView.as_view(), name='create_car'),
    path('car/update/<int:pk>', views.CarUpdateView.as_view(), name='update_car'),
    path('car/delete/<int:pk>', views.CarDeleteView.as_view(), name='delete_car'),
]
