from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('car/<int:pk>', views.CarView.as_view(), name='car'),
    path('car/create/', views.CarCreateView.as_view(), name='create_car'),
    path('car/update/<int:pk>', views.CarUpdateView.as_view(), name='update_car'),
    path('car/delete/<int:pk>', views.CarDeleteView.as_view(), name='delete_car'),
    path('car/<int:pk>/note/create/', views.NoteCreateView.as_view(), name='create_note'),
    path('car/<int:car_id>/note/update/<int:pk>/', views.NoteUpdateView.as_view(), name='update_note'),
    path('car/<int:car_id>/note/delete/<int:pk>/', views.NoteDeleteView.as_view(), name='delete_note'),
]
