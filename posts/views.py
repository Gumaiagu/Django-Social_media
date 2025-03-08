from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# Create your views here.
def posts_home(request):
    user = request.user
    if user.is_authenticated:
        user_object = User.objects.get(username=user)
        user_object.last_login = timezone.now()
        user_object.save()

        posts = list(Post.objects.all())
        posts.reverse()

        return render(request, 'posts/index.html', {'posts': posts[0:9]})
    else:
        return render(request, 'home/index.html')


def page(request, page):
    last_post_rendered = Post.objects.get(id=page)
    all_pages = list(Post.objects.all())
    all_pages.reverse()
    last_post_id = all_pages.index(last_post_rendered)

    start = last_post_id + 1
    end = start + 9
    return render(request, 'posts/new_posts.html', {'posts': all_pages[start:end]})


def create_posts(request):
    user = request.user
    banned = Group.objects.get(name='banned')
    is_banned = banned.user_set.filter(username=user).exists()
    if user.is_authenticated:
        if not is_banned:
            return render(request, 'posts/create_posts.html')
        else:
            return render(request, 'posts/is_banned.html')
    return redirect('home')


def new_post(request):
    if request.method == 'POST':
        content = request.POST

        image = ''
        if len(request.FILES) == 1:
            image = request.FILES['persons_file']
        title = content['title']
        text = content['description']
        user = request.user

        new_post = Post(title=title, user=user, text=text, image=image)
        new_post.save()
        return redirect('posts:home')
    

def likes(request, id):
    if request.method == "POST":
        post = Post.objects.get(id=id)
        post.likes += 1
        post.save()
        return HttpResponse(post.likes)


def dislikes(request, id):
    if request.method == "POST":
        post = Post.objects.get(id=id)
        post.dislikes += 1
        post.save()
        return HttpResponse(post.dislikes)
    

def delete(request, id):
    if request.method == "POST" and request.user.is_staff:
        post = Post.objects.get(id=id)
        if post.image:
            post.image.delete()
        post.delete()
        return HttpResponse('')
