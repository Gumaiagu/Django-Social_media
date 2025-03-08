from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/singup.html"


def user_profile(request, who):
    user = User.objects.get(username=who)
    banned = Group.objects.get(name='banned')
    is_banned = banned.user_set.filter(username=who).exists()
    return render(request, 'registration/user.html', {'who': user, "is_banned": is_banned})


def ban_user(request, banned_user_id):
    if request.method == 'POST' and request.user.is_staff:
        ban = Group.objects.get(name='banned')
        ban.user_set.add(banned_user_id)
        ban.save()
        return HttpResponse(f'<button hx-post="/unban_user/{banned_user_id}" hx-target="#ban-button" id="block">UnBan user</button>')
    

def unban_user(request, banned_user_id):
    if request.method == 'POST' and request.user.is_staff:
        user = User.objects.get(id=banned_user_id)
        user.groups.clear()
        return HttpResponse(f'<button hx-post="/ban_user/{banned_user_id}" hx-target="#ban-button" id="block">Ban user</button>')
