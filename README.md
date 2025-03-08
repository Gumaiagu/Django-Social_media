# Simple social media

This is a simple social media made in Django.

## Installation

First download the program files of this project, then create a virtual python environment and install these libraries into it using

```
pip install django Pillow
```

To execute, use

#### Unix/Mac OS

```
python3 manage.py runserver
```

#### Windows

```
py manage.py runserver
```

## User system

The user system was made using the Django user system.

There is a system of banning and deleting posts that I made, it's really simple, if the user has staff status (status that gives the user the ability to view the admin page, but not to modify it), the user has the ability to delete posts and ban users, it gives control of the site content to the site owners.

Unlike my chat site, we don't need to go to the admin page to delete posts or ban users, we can do it in the user about page and in the posts page.

To give to other users staff status, we need to have access to the admin page, so, create a super user with:

#### Unix/Mac OS

```
python3 manage.py createsuperuser
```

#### Windows

```
py manage.py createsuperuser
```

## Posts system

In this program, the aim was to create a social media like Instagram or X (an app with users and posts), so the main thing of the site is the posts.

There's a page where we can create posts, we can modify them:

* The title: text
* Description: text
* Image: image (can be blank)

There are 3 fixed statuses:

* User: a many to one relation (depends on which user created the post).
* Likes: integer (changes when someone clicks "like" on the post page).
* Dislikes: integer (changes when someone clicks "dislike" on the post page).

> We can give more than one like/dislike to a post.

>In the Posts page, I used an infinite scroll technique, like in 

As mentioned in the "User system" topic, there is a delete button, if the user has staff status, it will completely delete the post FOREVER, including the image (in an old version not published on Github, when a post was deleted, the image was not gone with the post).

## What I learned with this project

In this project, I learned about the difference between CBVs and FBVs in Django, I learned about HTMX and learned about infinite scrolls.

