from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('create/', views.review_create, name='review_create'),
    path('<int:review_id>/edit/', views.review_edit, name='review_edit'),
    path('<int:review_id>/delete/', views.review_delete, name='review_delete'),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('register/', views.register, name='register'),
    
] 
