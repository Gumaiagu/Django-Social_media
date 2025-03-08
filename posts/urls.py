from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.posts_home, name='home'),
    path('posts/posts/<int:page>', views.page, name='page'),

    path('posts/add_post', views.create_posts, name='add_posts'),
    path('posts/new_post', views.new_post, name='new_post'),
    path('posts/<str:id>/likes', views.likes, name='likes'),
    path('posts/<str:id>/dislikes', views.dislikes, name='dislikes'),
    path('posts/<str:id>/delete', views.delete, name='delete'),
]