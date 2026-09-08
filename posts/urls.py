from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('posts/<int:post_id>/like/', views.like_post, name='like_post'),
]